import { useState, useRef, useEffect } from "react";

import { useSidebar } from "./ui/sidebar";
import PromptInput from "./PromptInput";
import Message from "./Message";
import EmailDialog from "./EmailDialog";
import { useMutation } from "@tanstack/react-query";
import { sendMessage, type SendMessagePayload } from "@/lib/api";
import queryClient from "@/config/queryClient";
import { MESSAGE } from "@/hooks/useMessage";
import useMessage from "@/hooks/useMessage"


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

  const {
    mutate: send,
  } = useMutation({
    mutationFn: (payload: SendMessagePayload) => sendMessage(payload),
    onSuccess: (saved) => {
      const key = [MESSAGE, saved.userId];
      queryClient.setQueryData(key, (prev: any[]) => [...prev, saved]);
    },
  });

  const handleSend = () => {
    if (!message.trim() || !userId) return;
    send({ userId, role: "user", content: message });
    setMessage("")
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
      <div className="flex-1 overflow-y-auto pb-32">
        {messages.map((msg, index) => (
          <Message key={index} role={msg.role} content={msg.content} />
        ))}

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
