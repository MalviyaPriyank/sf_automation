
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarHeader,
} from "@/components/ui/sidebar"
import NavUser from "./NavUser";
import NavChat from "./NavChat";
import NavHeader from "./NavHeader";

export function AppSidebar() {
  return (
    <Sidebar>
      <SidebarHeader>
        <NavHeader/>
      </SidebarHeader>
      <SidebarContent>
        <NavChat/>
      </SidebarContent>
      <SidebarFooter>
        <NavUser/>
      </SidebarFooter>
    </Sidebar>
  )
}