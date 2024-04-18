/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./src/**/*.{html,js}"],
    theme: {
        margin: {
            sm: '8px',
            md: '16px',
            lg: '24px',
            decima: '10%',
            cuarto: '25%',
            xl: '30%',
        },
        colors: {
            'caoba': '#512C22',
            'verde': '#6b8e23',
            'celeste': '#87CEEB',
        },
        extend: {},
    },
    plugins: [],
}