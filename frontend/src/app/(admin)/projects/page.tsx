import Link from "next/link";

import PlaceholderContent from "@/components/placeholder";
import { ContentLayout } from "@/components/admin/content-layout";
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb";
// import { Card, CardContent } from "@/components/ui/card";
// import MessageBox from "@/components/chat/message-box";
// import Chat from "@/components/chat/chat";
// import AgentCard from "@/components/admin-panel/agent-card";
// import AgentPage from "@/components/agent/agent-page";

export default function AssistantPage() {
  return (
    <ContentLayout title="Agents">
      <Breadcrumb>
        <BreadcrumbList>
          <BreadcrumbItem>
            <BreadcrumbLink asChild>
              <Link href="/">Home</Link>
            </BreadcrumbLink>
          </BreadcrumbItem>
          <BreadcrumbSeparator />
          <BreadcrumbItem>
            <BreadcrumbPage>Agents</BreadcrumbPage>
          </BreadcrumbItem>
        </BreadcrumbList>
      </Breadcrumb>

      <PlaceholderContent />
    </ContentLayout>
  );
}
