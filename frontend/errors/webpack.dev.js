const {merge} = require('webpack-merge');
const common = require('./webpack.common.js');
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

const outputPath = './build/';
const srcPath = './src/';

module.exports = merge(common, {
    mode: 'development',
    devServer: {
        compress: false,
        port: 4580
    },
    devtool: 'cheap-source-map',
    output: {
        path: path.join(__dirname, outputPath),
        filename: '[name].[fullhash].js'
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: [{loader: 'babel-loader'}]
            },
            {
                test: /\.scss$/,
                use: [
                    {loader: 'style-loader'},
                    {loader: 'css-loader'},
                    {loader: 'sass-loader'}]
            }

        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
            title: 'My App',
            filename: 'error.html',
            template: path.join(__dirname, srcPath + 'error.html'),
            minify: false
        }),
    ],
});
