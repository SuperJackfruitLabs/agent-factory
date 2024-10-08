import { PanelsTopLeft, Bot, LogIn } from "lucide-react";
import Link from "next/link";
import Image from "next/image";
import { ArrowRightIcon, GitHubLogoIcon } from "@radix-ui/react-icons";

import { Button } from "@/components/ui/button";
import { ModeToggle } from "@/components/mode-toggle";
// import { SignInButton, SignedIn, SignedOut, UserButton } from "@clerk/nextjs";

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen">
      <header className="z-[50] sticky top-0 w-full bg-background/95 border-b backdrop-blur-sm dark:bg-black/[0.6] border-border/40">
        <div className="container h-14 flex items-center">
          <Link
            href=""
            className="flex justify-start items-center hover:opacity-85 transition-opacity duration-300"
          >
            <Bot className="w-6 h-6 mr-3" />
            <span className="font-bold">Agent Factory</span>
            <span className="sr-only">Agent Factory</span>
          </Link>
          <nav className="ml-auto flex items-center gap-2">
            <Button
              variant="outline"
              size="icon"
              className="rounded-full w-8 h-8 bg-background"
              asChild
            >
              <Link href="https://github.com/rakeshgangwar">
                <GitHubLogoIcon className="w-[1.2rem] h-[1.2rem]" />
              </Link>
            </Button>
            <ModeToggle />
            {/* <SignedOut>
              <SignInButton />
            </SignedOut>
            <SignedIn>
              <UserButton />
            </SignedIn> */}
          </nav>
        </div>
      </header>
      <main className="min-h-[calc(100vh-57px-97px)] flex-1">
        <div className="container relative pb-10">
          <section className="mx-auto flex max-w-[980px] flex-col items-center gap-2 py-8 md:py-12 md:pb-8 lg:py-24 lg:pb-6">
            <h1 className="text-center text-3xl font-bold leading-tight tracking-tighter md:text-5xl lg:leading-[1.1]">
              Building Future Workforce
            </h1>
            <span className="max-w-[750px] text-center text-lg font-light text-foreground">
              Transform ideas into intelligent solutions with Agent Factory.
              Build and deploy AI agents effortlessly using our intuitive
              platform. Start your AI journey today!
            </span>
            <div className="flex w-full items-center justify-center space-x-4 py-4 md:pb-6">
              {/* <SignedIn>
                <Button variant="default" asChild>
                  <Link href="/dashboard">
                    Dashboard
                    <ArrowRightIcon className="ml-2" />
                  </Link>
                </Button>
              </SignedIn> */}

              {/* <SignedOut>
                <SignInButton>
                  <Button variant="default">
                    Sign In
                    <LogIn className="w-4 h-4 ml-2" />
                  </Button>
                </SignInButton>
              </SignedOut> */}

              {/* <Button variant="outline" asChild>
                <Link
                  href="https://ui.shadcn.com/"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  Learn about us
                </Link>
              </Button> */}
            </div>
          </section>
          <div className="w-full flex justify-center relative">
            <Image
              src="/female-agent-light-mode.jpeg"
              width={500}
              height={400}
              alt="demo"
              priority
              className="shadow-sm dark:hidden"
            />
            <Image
              src="/female-agent.jpeg"
              width={500}
              height={400}
              alt="demo-dark"
              priority
              className="hidden dark:block dark:shadow-gray-500/5"
            />
            {/* <Image
              src="/demo-mobile-light-min.png"
              width={228}
              height={494}
              alt="demo-mobile"
              className="border rounded-xl absolute bottom-0 right-0 hidden lg:block dark:hidden"
            />
            <Image
              src="/demo-mobile-dark-min.png"
              width={228}
              height={494}
              alt="demo-mobile"
              className="border border-zinc-600 rounded-xl absolute bottom-0 right-0 hidden dark:lg:block"
            /> */}
          </div>
        </div>
      </main>
      <footer className="py-6 md:py-0 border-t border-border/40">
        <div className="container flex flex-col items-center justify-center gap-4 md:h-24 md:flex-row">
          <p className="text-balance text-center text-sm leading-loose text-muted-foreground">
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
      </footer>
    </div>
  );
}
