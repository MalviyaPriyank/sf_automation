import { deleteConversations, type Conversation } from "@/lib/api"
import { useMutation, useQueryClient } from "@tanstack/react-query"
import { CONVERSATION } from "./useConversation";


const useDeleteConversation = (conversationId: Conversation["_id"]) => {
  const queryClient = useQueryClient();
  const userId =
    typeof window !== "undefined" ? localStorage.getItem("user_id") : null;
  const queryKey = userId ? [CONVERSATION, userId] : [CONVERSATION];

  const {mutate, ...rest} = useMutation({
    mutationFn: () => deleteConversations(conversationId),
    onSuccess: () => 
      queryClient.setQueryData<Conversation[]>(queryKey, (cache) =>
        (cache ?? []).filter((conversation) => conversation._id !== conversationId))
  })

  return {deleteConversation: mutate, ...rest}
}

export default useDeleteConversation;
