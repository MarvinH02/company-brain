// TODO(M1): global styles (Tailwind or CSS modules - your call), font, <AuthProvider>.
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
