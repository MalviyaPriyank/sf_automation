import { useState, useRef, useEffect } from "react";

import { useSidebar } from "./ui/sidebar";
import PromptInput from "./PromptInput";
import Message from "./Message";
import EmailDialog from "./EmailDialog";
import { useMutation } from "@tanstack/react-query";
import {
  sendMessage,
  type SendMessagePayload,
  type Message as ApiMessage,
} from "@/lib/api";
import queryClient from "@/config/queryClient";
import { MESSAGE } from "@/hooks/useMessage";
import useMessage from "@/hooks/useMessage";
import { Spinner } from "./ui/spinner";
import { Badge } from "./ui/badge";

// type MessageType = {
//   role: "user" | "assistant";
//   content: string;
// };

const Chat = () => {
  const userId =
    typeof window !== "undefined" ? localStorage.getItem("user_id") : null;

  const { state, isMobile } = useSidebar();

  const [message, setMessage] = useState("");
  // const [messages, setMessages] = useState<MessageType[]>([]);

  const inputRef = useRef<HTMLTextAreaElement>(null);
  const bottomRef = useRef<HTMLDivElement | null>(null);

  const getLeftPadding = () => {
    if (isMobile) return "1rem";
    return state === "expanded" ? "calc(var(--sidebar-width) + 1rem)" : "1rem";
  };

  // const { data: messages = [], isLoading } = useMessages(userId);
  // const { mutate: send, isPending } = useSendMessage();

  const { messages = [] } = useMessage();
  const queryKey = [MESSAGE, userId];

  const { mutate: send, isPending } = useMutation({
    mutationFn: (payload: SendMessagePayload) => sendMessage(payload),
    onMutate: async (payload) => {
      if (!userId) return;

      await queryClient.cancelQueries({ queryKey });
      const previous = queryClient.getQueryData<ApiMessage[]>(queryKey) || [];

      const optimistic: ApiMessage = {
        _id: Date.now().toString(),
        userId: payload.userId,
        role: payload.role,
        content: payload.content,
      };

      queryClient.setQueryData<ApiMessage[]>(queryKey, [
        ...previous,
        optimistic,
      ]);

      return { previous, tempId: optimistic._id };
    },
    onError: (_err, _payload, context) => {
      if (context?.previous) {
        queryClient.setQueryData(queryKey, context.previous);
      }
    },
    onSuccess: (saved, _payload, context) => {
      if (!context) return;

      queryClient.setQueryData<ApiMessage[]>(queryKey, (prev = []) =>
        prev.map((msg) => (msg._id === context.tempId ? saved : msg))
      );
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey });
    },
  });

  const handleSend = () => {
    if (!message.trim() || !userId) return;
    send({ userId, role: "user", content: message });
    setMessage("");
  };

  // Auto-focus textarea when user starts typing and nothing is focused
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key.length === 1 && !e.ctrlKey && !e.metaKey && !e.altKey) {
        const activeElement = document.activeElement;
        if (
          activeElement?.tagName !== "INPUT" &&
          activeElement?.tagName !== "TEXTAREA"
        ) {
          inputRef.current?.focus();
        }
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, []);

  // Smooth scroll to bottom whenever messages change
  useEffect(() => {
    if (bottomRef.current) {
      bottomRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [messages]);

  return (
    <>
      <div className="flex-1 overflow-y-auto pb-40">
        {messages.map((msg, index) => (
          <Message key={index} role={msg.role} content={msg.content} />
        ))}

        {isPending && (
          <div className="max-w-4xl mx-auto">
            <Badge variant="outline">
              <Spinner className="size-5" />
              Processing
            </Badge>
          </div>
        )}

        {/* Dummy div to scroll into view */}
        <div ref={bottomRef} />
      </div>

      <div
        className="fixed bottom-0 left-0 right-0 p-4 transition-all duration-200 ease-linear"
        style={{ paddingLeft: getLeftPadding() }}
      >
        <div className="max-w-4xl mx-auto bg-background rounded-lg">
          <PromptInput
            ref={inputRef}
            message={message}
            onMessageChange={setMessage}
            onSend={handleSend}
            disabled={!message.trim()}
          />
        </div>
      </div>

      <EmailDialog />
    </>
  );
};

export default Chat;
