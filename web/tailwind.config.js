/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./divers/templates/divers/*.html",
    "./templates/*.html",
    "./templates/includes/*.html"
  ],
  theme: {
    screens: {
      sm: "530px",
      md: "768px",
      lg: "976px",
      xl: "1300px"
    },
    extend: {
      colors: {
        ResedaGreen: "hsl(129, 8%, 53%)",
        Onyx: "hsl(154, 7%, 19%)",
        MountbattenPink: "hsl(282, 10%, 56%)",
        FrenchGray: "hsl(219, 22%, 82%)",
        CadetGray: "hsl(207, 10%, 66%)",
      },
      spacing: {
        big:"48rem"
      }
    },
  },
  plugins: [],
};
