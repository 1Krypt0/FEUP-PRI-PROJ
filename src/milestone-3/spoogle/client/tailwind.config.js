/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        snred: "#ee1c25",
        snblack: "#303030",
      },
      fontFamily: {
        sn: ["Teko", "sans-serif"],
      },
    },
  },
  plugins: [],
};
