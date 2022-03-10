const path = require('path');
const {CleanWebpackPlugin} = require('clean-webpack-plugin');

let cleanOptions = {
    root: path.join(__dirname, ''),
    verbose: true,
    dry: false
};

const srcPath = './src/';
module.exports = {
    entry: {
        app: path.join(__dirname, srcPath + 'app.js')
    },
    module: {
        rules: [
            {
                test: /\.html$/i,
                loader: 'html-loader',
                options: {
                    minimize: false,
                    sources: {
                        list: [
                            {
                                tag: 'img',
                                attribute: 'src',
                                type: 'src',
                            },
                            {
                                tag: 'image',
                                attribute: 'xlink:href',
                                type: 'src',
                            },
                        ]}
                }
            },
            {
                test: /\.(woff|woff2|eot|ttf|otf)$/,
                exclude: /node_modules/,
                type: 'asset/resource',
            },
            {
                test: /\.(png|svg|jpg|gif)$/,
                exclude: /node_modules/,
                type: 'asset/resource',
            },
        ]
    },
    plugins: [
        new CleanWebpackPlugin(cleanOptions),
    ]
}
