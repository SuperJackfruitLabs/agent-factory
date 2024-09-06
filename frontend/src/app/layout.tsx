import type { Metadata } from "next";
import { GeistSans } from "geist/font/sans";
import "./globals.css";
import { ThemeProvider } from "@/providers/theme-provider";

// const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Agent Factory",
  description:
    "Transform ideas into intelligent solutions with Agent Factory. Build and deploy AI agents effortlessly using our intuitive platform. Start your AI journey today!",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={GeistSans.className}>
        <ThemeProvider attribute="class" defaultTheme="system" enableSystem>
          {children}
        </ThemeProvider>
      </body>
    </html>
  );
}
