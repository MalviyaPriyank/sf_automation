import {
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarMenuSkeleton,
} from "./ui/sidebar";
import useConversation from "@/hooks/useConversation";
import ChatDropdownMenu from "./ChatDropdownMenu";

const NavChat = () => {
  const { conversations, isPending, isError } = useConversation();
  const conversationList = conversations ?? [];

  return (
    <SidebarGroup>
      <SidebarGroupLabel>Chats</SidebarGroupLabel>
      <SidebarGroupContent>
        {isPending ? (
          <ChatListSkeleton />
        ) : isError ? (
          <p className="px-2 text-sm text-destructive">Failed to load chats.</p>
        ) : conversationList.length ? (
          <SidebarMenu>
            {conversationList.map((conversation) => (
              <SidebarMenuItem key={conversation._id}>
                <SidebarMenuButton asChild>
                  <a href="#">
                    <span>{conversation.title}</span>
                  </a>
                </SidebarMenuButton>
                <ChatDropdownMenu conversation={conversation} />
              </SidebarMenuItem>
            ))}
          </SidebarMenu>
        ) : (
          <EmptyState />
        )}
      </SidebarGroupContent>
    </SidebarGroup>
  );
};

function ChatListSkeleton({ count = 3 }: { count?: number }) {
  return (
    <SidebarMenu>
      {Array.from({ length: count }).map((_, index) => (
        <SidebarMenuItem key={index}>
          <SidebarMenuSkeleton showIcon />
        </SidebarMenuItem>
      ))}
    </SidebarMenu>
  );
}

function EmptyState() {
  return (
    <p className="px-2 text-sm text-muted-foreground">No chats yet.</p>
  );
}

export default NavChat;
