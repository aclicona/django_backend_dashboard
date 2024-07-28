/** @type {import('tailwindcss').Config} */
// eslint-disable-next-line no-undef
const colors = require('tailwindcss/colors')
export default {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}'
  ],
  theme: {
    extend: {
      colors: {
        main: colors.purple,
        alt: colors.pink,
        third: colors.emerald,
        neutral: colors.gray
      }
    },
    minHeight: {
      '28': '7rem',
      'screen': '100vh'
    },
    maxHeight: {
      '90p': '90%',
      '60vh': '60vh'
    },
    minWidth: {
      '1rem': '1rem',
      'tareasMd': '115%',
      'tareas2xl': '100%'
    },
    maxWidth: {
      'inputlabel': 'calc(100% - 1rem)'
    }
  },
  plugins: []
}
