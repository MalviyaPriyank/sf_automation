import { MoreHorizontal, Trash2 } from "lucide-react"

import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuAction,
  SidebarMenuButton,
  SidebarMenuItem,
} from "@/components/ui/sidebar"
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger } from "./ui/dropdown-menu"
import NavUser from "./NavUser";
import NavChat from "./NavChat";
import NavHeader from "./NavHeader";

const data = {
  user: {
    name: "John Smith",
    email: "johnsmith@example.com",
    avatar: "/avatars/shadcn.jpg",
  },
  navChat: [
    {
      title: "Snowflake Roles Overview",
      url: "#",
    },
    {
      title: "Create Common Snowflake Roles",
      url: "#",
    },
    {
      title: "Explain Role Configurations",
      url: "#",
    },
    {
      title: "Design Role Hierarchy Ideas",
      url: "#",
    },
    {
      title: "Read-Only vs Analyst Roles",
      url: "#",
    },
    {
      title: "Plan Security Admin Permissions",
      url: "#",
    },
    {
      title: "Snowflake Security Integration Basics",
      url: "#",
    },
    {
      title: "Sample Azure AD SSO Integration",
      url: "#",
    },
    {
      title: "Sample Okta SSO Integration",
      url: "#",
    },
    {
      title: "OAuth Integration Requirements",
      url: "#",
    },
    {
      title: "Intro to Snowflake Streams",
      url: "#",
    },
    {
      title: "Plan Demo Streams Environment",
      url: "#",
    },
    {
      title: "Create STREAMS_DEMO_DB Schema",
      url: "#",
    },
    {
      title: "Troubleshoot Table Creation Errors",
      url: "#",
    },
    {
      title: "Design Simple Orders Table",
      url: "#",
    },
    {
      title: "SQL for Demo Orders and Customers",
      url: "#",
    },
    {
      title: "Standard vs Append-Only Streams",
      url: "#",
    },
    {
      title: "Create Streams on Demo Tables",
      url: "#",
    },
    {
      title: "Test Streams with Sample Data",
      url: "#",
    },
    {
      title: "Show SQL for Stream Setup",
      url: "#",
    },
    {
      title: "Define E-commerce Demo Schema",
      url: "#",
    },
    {
      title: "Create Customers Table Design",
      url: "#",
    },
    {
      title: "Create Products and Categories Tables",
      url: "#",
    },
    {
      title: "Create Orders and Order_Items Tables",
      url: "#",
    },
    {
      title: "Add Streams to All Core Tables",
      url: "#",
    },
    {
      title: "Verify Tables in SALES_DATA Schema",
      url: "#",
    },
    {
      title: "Clarify What’s Actually Created",
      url: "#",
    },
    {
      title: "Manual SQL Execution in Snowflake",
      url: "#",
    },
    {
      title: "Next Steps for Demo Data Model",
      url: "#",
    },
    {
      title: "Recap Snowflake Demo Environment",
      url: "#",
    },
  ],
}

export function AppSidebar() {
  return (
    <Sidebar>
      <SidebarHeader>
        <NavHeader/>
      </SidebarHeader>
      <SidebarContent>
        <NavChat items={data.navChat}/>
      </SidebarContent>
      <SidebarFooter>
        <NavUser user={data.user} />
      </SidebarFooter>
    </Sidebar>
  )
}