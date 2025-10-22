/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        activeSidebarItemBg: "#d7ebff",
        hoverSidebarItemBg: "#e8f3ff",
        primaryBg: "#f5f7fa",
        secondaryBg: "#FFFFFF",
        tertiaryBg: "#E4E9F0",
        navBg: "#1F2937",
        activeNav: "#3B82F6",
      },
    },
  },
  plugins: [],
};
