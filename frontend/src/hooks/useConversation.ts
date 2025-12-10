import { type Conversation, getConversations } from "@/lib/api";
import { useQuery } from "@tanstack/react-query";

export const CONVERSATION = "conversation";

const useConversation = () => {
  const userId =
    typeof window !== "undefined" ? localStorage.getItem("user_id") : null;

  const { data: conversations, isError, ...rest } = useQuery<Conversation[]>({
    queryKey: [CONVERSATION, userId],
    queryFn: () => getConversations(userId!),
    enabled: !!userId,
    refetchOnWindowFocus: false,
    select: (data) => [...data].reverse(),
  });

  return {
    conversations,
    isError,
    ...rest,
  };
};

export default useConversation;
