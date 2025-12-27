// frontend/src/hooks/useMessage.ts

import { getMessages, type Message } from "@/lib/api";
import { useQuery } from "@tanstack/react-query";

export const MESSAGE = "message";

const useMessage = () => {
  const userId =
    typeof window !== "undefined" ? localStorage.getItem("user_id") : null;

  const {
    data: messages,
    isError,
    ...rest
  } = useQuery<Message[]>({
    queryKey: [MESSAGE, userId],
    queryFn: () => getMessages(userId!),
    enabled: !!userId,
    refetchOnWindowFocus: false,
    refetchInterval: 2000,
  });

  return {
    messages,
    isError,
    ...rest
  }
};

export default useMessage;
