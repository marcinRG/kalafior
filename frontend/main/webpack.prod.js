const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const {WebpackManifestPlugin} = require('webpack-manifest-plugin');
const {merge} = require('webpack-merge');
const common = require('./webpack.common.js');


const srcPath = './src/';
const outPath = './dist/';
const staticPath = './static/main/';

module.exports = merge(common, {
    mode: 'production',
    output: {
        clean: true,
        path: path.join(__dirname, path.join(outPath, staticPath)),
        filename: '[name].js',
        assetModuleFilename: 'assets/[name][ext]'
    },
    optimization: {
        minimize: true
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
                    {
                        loader: MiniCssExtractPlugin.loader
                    },
                    {
                        loader: 'css-loader'
                    },
                    {
                        loader: 'postcss-loader',
                    },
                    {
                        loader: 'sass-loader',
                    }]
            }
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
            title: 'My App',
            filename: './../../index.html',
            template: path.join(__dirname, srcPath + 'index.html'),
            minify: false
        }),
        new MiniCssExtractPlugin({
            filename: 'style.css'
        }),
        new WebpackManifestPlugin({})
    ],
});