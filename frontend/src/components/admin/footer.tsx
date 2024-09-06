import Link from "next/link";
import { Avatar, AvatarImage } from "@/components/ui/avatar";

export function Footer() {
  return (
    <div className="z-20 w-full bg-background/95 shadow backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="mx-4 md:mx-8 flex h-14 items-center">
        <p className="text-xs md:text-sm leading-loose text-muted-foreground text-left">
          Built with &#x2764; in India. Designed by{" "}
          <Link
            href="https://superjackfruit.com"
            target="_blank"
            rel="noopener noreferrer"
            className="font-medium underline underline-offset-4"
          >
            Super Jackfruit Labs (OPC) Pvt. Ltd.
          </Link>
          .
        </p>
      </div>
    </div>
  );
}
