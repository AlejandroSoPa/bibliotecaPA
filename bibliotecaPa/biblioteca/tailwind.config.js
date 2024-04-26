/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["templates/**/*.html", "static/**/*.css"],
    theme: {
        margin: {
            sm: '8px',
            md: '16px',
            lg: '5%',
            decima: '10%',
            cuarto: '25%',
            xl: '30%',
        },
        colors: {
            'caoba': '#5a3d35',
            'verde': '#6b8e23',
            'celeste': '#87CEEB',
            'textWhite': '#FFFFFF',
            'marron': '#6c4f47'
        },
        extend: {
            gridTemplateRows: {
                'layout': 'auto auto auto',
            },
            
        },
    },
    plugins: [],
}
