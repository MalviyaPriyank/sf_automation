import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "./ui/dropdown-menu";
import { Ellipsis, Trash2 } from "lucide-react";
import { SidebarMenuAction } from "./ui/sidebar";
import type { Conversation } from "@/lib/api";
import useDeleteConversation from "@/hooks/useDeleteConversation";

interface Props {
  conversation: Conversation;
}

const ChatDropdownMenu = ({ conversation }: Props) => {
  const { _id } = conversation;
  const { deleteConversation, isPending } = useDeleteConversation(_id);
  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <SidebarMenuAction showOnHover disabled={isPending} aria-label="Conversation actions">
          <Ellipsis />
        </SidebarMenuAction>
      </DropdownMenuTrigger>
      <DropdownMenuContent side="right" align="start">
        <DropdownMenuItem
          variant="destructive"
          disabled={isPending}
          onClick={() => deleteConversation()}
        >
          <Trash2 />
          <span>{isPending ? "Deleting..." : "Delete"}</span>
        </DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  );
};

export default ChatDropdownMenu;
