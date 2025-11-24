# Webpack Configuration Optimizer

**Optimize webpack builds for maximum performance and minimal bundle size.**

**IMPORTANT: Analyze and optimize webpack configuration for production builds.**

---

╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║            SENA 🦁 WEBPACK CONFIG OPTIMIZER v3.3                     ║
║      Build Speed · Bundle Size · Code Splitting · Optimization       ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝

════════════════════════════════════════════════════════════════════════
  BUILD PERFORMANCE OVERVIEW
════════════════════════════════════════════════════════════════════════

**Current Build Metrics:**

┌────────────────────────────────────────────────────────────────────┐
│ Metric                 │ Current │ Optimal │ Status              │
├────────────────────────────────────────────────────────────────────┤
│ Build Time (dev)       │ 45s     │ < 10s   │ 🔴 Too Slow         │
│ Build Time (prod)      │ 3m 24s  │ < 1m    │ 🔴 Too Slow         │
│ Bundle Size            │ 1.8 MB  │ < 500KB │ 🔴 Too Large        │
│ Chunks                 │ 3       │ 10-15   │ 🔴 Under-split      │
│ Cache Usage            │ 0%      │ 90%+    │ 🔴 Not Cached       │
│ Tree Shaking           │ 23%     │ 95%+    │ 🔴 Poor             │
└────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════
  OPTIMIZED WEBPACK CONFIGURATION
════════════════════════════════════════════════════════════════════════

**Production Configuration:**

```javascript
// webpack.config.js - Optimized for performance
const path = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin');
const TerserPlugin = require('terser-webpack-plugin');
const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');
const CompressionPlugin = require('compression-webpack-plugin');
const WorkboxPlugin = require('workbox-webpack-plugin');
const ForkTsCheckerWebpackPlugin = require('fork-ts-checker-webpack-plugin');

const isDev = process.env.NODE_ENV === 'development';
const isProd = !isDev;

module.exports = {
  mode: isProd ? 'production' : 'development',

  // ✅ Entry points with code splitting
  entry: {
    main: './src/index.tsx',
    // Vendor splitting handled by optimization.splitChunks
  },

  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: isProd
      ? '[name].[contenthash:8].js'
      : '[name].bundle.js',
    chunkFilename: isProd
      ? '[name].[contenthash:8].chunk.js'
      : '[name].chunk.js',
    clean: true,
    assetModuleFilename: 'assets/[hash][ext][query]',
  },

  // ✅ Advanced optimization
  optimization: {
    minimize: isProd,
    minimizer: [
      // JavaScript minification
      new TerserPlugin({
        terserOptions: {
          parse: { ecma: 8 },
          compress: {
            ecma: 5,
            warnings: false,
            comparisons: false,
            inline: 2,
            drop_console: isProd,
            drop_debugger: isProd,
            pure_funcs: isProd ? ['console.log'] : [],
          },
          mangle: { safari10: true },
          output: {
            ecma: 5,
            comments: false,
            ascii_only: true,
          },
        },
        parallel: true,
      }),

      // CSS minification
      new CssMinimizerPlugin({
        minimizerOptions: {
          preset: [
            'default',
            {
              discardComments: { removeAll: true },
              normalizeUnicode: false,
            },
          ],
        },
      }),
    ],

    // ✅ Advanced code splitting
    splitChunks: {
      chunks: 'all',
      maxInitialRequests: 25,
      minSize: 20000,
      maxSize: 244000,
      cacheGroups: {
        // Vendor libraries
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name(module) {
            const packageName = module.context.match(
              /[\\/]node_modules[\\/](.*?)([\\/]|$)/
            )[1];
            return `vendor.${packageName.replace('@', '')}`;
          },
          priority: 10,
        },

        // React specific
        react: {
          test: /[\\/]node_modules[\\/](react|react-dom|react-router)[\\/]/,
          name: 'react',
          priority: 20,
          enforce: true,
        },

        // UI components library
        ui: {
          test: /[\\/]node_modules[\\/](@mui|@emotion|styled-components)[\\/]/,
          name: 'ui-lib',
          priority: 15,
        },

        // Async chunks
        async: {
          test: /[\\/]src[\\/]pages[\\/]/,
          name: 'async',
          chunks: 'async',
          priority: 5,
        },

        // Common modules
        common: {
          minChunks: 2,
          priority: -10,
          reuseExistingChunk: true,
        },
      },
    },

    // Module IDs for long-term caching
    moduleIds: 'deterministic',
    runtimeChunk: 'single',

    // Tree shaking
    usedExports: true,
    sideEffects: false,
  },

  // ✅ Module resolution
  resolve: {
    extensions: ['.tsx', '.ts', '.jsx', '.js', '.json'],
    alias: {
      '@': path.resolve(__dirname, 'src'),
      '@components': path.resolve(__dirname, 'src/components'),
      '@utils': path.resolve(__dirname, 'src/utils'),
      '@hooks': path.resolve(__dirname, 'src/hooks'),
      '@styles': path.resolve(__dirname, 'src/styles'),
    },
    // Prefer ES modules for tree shaking
    mainFields: ['module', 'main'],
  },

  // ✅ Module rules
  module: {
    rules: [
      // TypeScript/JavaScript
      {
        test: /\.(ts|tsx|js|jsx)$/,
        exclude: /node_modules/,
        use: [
          // Babel loader with caching
          {
            loader: 'babel-loader',
            options: {
              cacheDirectory: true,
              cacheCompression: false,
              presets: [
                ['@babel/preset-env', {
                  useBuiltIns: 'entry',
                  corejs: 3,
                  modules: false,
                }],
                '@babel/preset-react',
                '@babel/preset-typescript',
              ],
              plugins: [
                isDev && 'react-refresh/babel',
                isProd && ['transform-remove-console', {
                  exclude: ['error', 'warn'],
                }],
              ].filter(Boolean),
            },
          },
        ],
      },

      // CSS/SCSS
      {
        test: /\.(css|scss|sass)$/,
        use: [
          isProd ? MiniCssExtractPlugin.loader : 'style-loader',
          {
            loader: 'css-loader',
            options: {
              importLoaders: 2,
              modules: {
                auto: true,
                localIdentName: isProd
                  ? '[hash:base64:8]'
                  : '[path][name]__[local]',
              },
            },
          },
          {
            loader: 'postcss-loader',
            options: {
              postcssOptions: {
                plugins: [
                  'postcss-preset-env',
                  isProd && ['cssnano', { preset: 'default' }],
                ].filter(Boolean),
              },
            },
          },
          'sass-loader',
        ],
      },

      // Images
      {
        test: /\.(png|svg|jpg|jpeg|gif|webp)$/i,
        type: 'asset',
        parser: {
          dataUrlCondition: {
            maxSize: 8 * 1024, // 8kb
          },
        },
        generator: {
          filename: 'images/[name].[hash:8][ext]',
        },
      },

      // Fonts
      {
        test: /\.(woff|woff2|eot|ttf|otf)$/i,
        type: 'asset/resource',
        generator: {
          filename: 'fonts/[name].[hash:8][ext]',
        },
      },
    ],
  },

  // ✅ Plugins
  plugins: [
    // HTML generation
    new HtmlWebpackPlugin({
      template: './public/index.html',
      inject: true,
      minify: isProd ? {
        removeComments: true,
        collapseWhitespace: true,
        removeRedundantAttributes: true,
        useShortDoctype: true,
        removeEmptyAttributes: true,
        removeStyleLinkTypeAttributes: true,
        keepClosingSlash: true,
        minifyJS: true,
        minifyCSS: true,
        minifyURLs: true,
      } : false,
    }),

    // CSS extraction
    isProd && new MiniCssExtractPlugin({
      filename: 'css/[name].[contenthash:8].css',
      chunkFilename: 'css/[name].[contenthash:8].chunk.css',
    }),

    // Type checking in separate process
    new ForkTsCheckerWebpackPlugin({
      async: isDev,
      typescript: {
        configOverwrite: {
          compilerOptions: {
            skipLibCheck: true,
            sourceMap: isDev,
            inlineSourceMap: false,
            declarationMap: false,
          },
        },
      },
    }),

    // Environment variables
    new webpack.DefinePlugin({
      'process.env.NODE_ENV': JSON.stringify(process.env.NODE_ENV),
    }),

    // Bundle analyzer (only in analyze mode)
    process.env.ANALYZE && new BundleAnalyzerPlugin({
      analyzerMode: 'static',
      openAnalyzer: false,
      reportFilename: 'bundle-report.html',
    }),

    // Compression
    isProd && new CompressionPlugin({
      test: /\.(js|css|html|svg)$/,
      algorithm: 'gzip',
      threshold: 10240,
      minRatio: 0.8,
    }),

    isProd && new CompressionPlugin({
      test: /\.(js|css|html|svg)$/,
      algorithm: 'brotliCompress',
      threshold: 10240,
      minRatio: 0.8,
      filename: '[path][base].br',
    }),

    // Service Worker
    isProd && new WorkboxPlugin.GenerateSW({
      clientsClaim: true,
      skipWaiting: true,
      runtimeCaching: [
        {
          urlPattern: /^https:\/\/api\./,
          handler: 'NetworkFirst',
          options: {
            cacheName: 'api-cache',
            expiration: {
              maxEntries: 50,
              maxAgeSeconds: 5 * 60, // 5 minutes
            },
          },
        },
        {
          urlPattern: /\.(png|jpg|jpeg|svg|gif)$/,
          handler: 'CacheFirst',
          options: {
            cacheName: 'image-cache',
            expiration: {
              maxEntries: 100,
              maxAgeSeconds: 30 * 24 * 60 * 60, // 30 days
            },
          },
        },
      ],
    }),

    // Module concatenation
    new webpack.optimize.ModuleConcatenationPlugin(),
  ].filter(Boolean),

  // ✅ Dev server configuration
  devServer: isDev ? {
    hot: true,
    port: 3000,
    open: true,
    compress: true,
    historyApiFallback: true,
    client: {
      overlay: {
        errors: true,
        warnings: false,
      },
    },
  } : undefined,

  // ✅ Performance hints
  performance: {
    hints: isProd ? 'warning' : false,
    maxEntrypointSize: 512000,
    maxAssetSize: 512000,
  },

  // ✅ Source maps
  devtool: isDev ? 'eval-cheap-module-source-map' : 'source-map',

  // ✅ Caching
  cache: {
    type: 'filesystem',
    allowCollectingMemory: true,
    buildDependencies: {
      config: [__filename],
    },
  },

  // ✅ Stats
  stats: {
    colors: true,
    hash: false,
    version: false,
    timings: true,
    assets: true,
    chunks: false,
    modules: false,
    reasons: false,
    children: false,
    source: false,
    errors: true,
    errorDetails: true,
    warnings: true,
    publicPath: false,
  },
};
```

════════════════════════════════════════════════════════════════════════
  BUILD SPEED OPTIMIZATION
════════════════════════════════════════════════════════════════════════

**Speed Improvements:**

```javascript
// ✅ Development Speed Optimizations
const devConfig = {
  // Use eval for faster rebuilds
  devtool: 'eval-cheap-module-source-map',

  // Skip production optimizations
  optimization: {
    removeAvailableModules: false,
    removeEmptyChunks: false,
    splitChunks: false,
  },

  // Faster TypeScript checking
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        loader: 'esbuild-loader',
        options: {
          loader: 'tsx',
          target: 'es2015',
        },
      },
    ],
  },

  // Cache everything
  cache: {
    type: 'memory',
  },
};

// ✅ Build Performance Monitoring
class BuildSpeedPlugin {
  apply(compiler) {
    let startTime;

    compiler.hooks.compile.tap('BuildSpeedPlugin', () => {
      startTime = Date.now();
      console.log('Build started...');
    });

    compiler.hooks.done.tap('BuildSpeedPlugin', (stats) => {
      const duration = Date.now() - startTime;
      console.log(`Build completed in ${duration}ms`);

      if (duration > 60000) {
        console.warn('⚠️ Build took more than 1 minute!');
      }
    });
  }
}
```

════════════════════════════════════════════════════════════════════════
  BUNDLE SIZE ANALYSIS
════════════════════════════════════════════════════════════════════════

**Bundle Composition:**

```
Current Bundle (1.8MB):
├─ vendor.react (125KB)
├─ vendor.mui (342KB)
├─ vendor.lodash (89KB)
├─ vendor.moment (127KB)
├─ main (487KB)
├─ runtime (12KB)
└─ css (618KB)

After Optimization (489KB):
├─ react (42KB)
├─ ui-lib (89KB)
├─ vendor.core (67KB)
├─ main (123KB)
├─ async.* (45KB)
├─ runtime (8KB)
└─ css (115KB)
```

**Size Reduction Strategies:**

```javascript
// ✅ Dynamic imports for code splitting
const Dashboard = lazy(() =>
  import(/* webpackChunkName: "dashboard" */ './pages/Dashboard')
);

// ✅ Tree-shakeable imports
import { debounce } from 'lodash-es'; // NOT: import _ from 'lodash'

// ✅ Production-only dependencies
if (process.env.NODE_ENV === 'production') {
  require('./analytics');
}
```

════════════════════════════════════════════════════════════════════════
  PERFORMANCE METRICS
════════════════════════════════════════════════════════════════════════

**Build Performance Comparison:**

┌────────────────────────────────────────────────────────────────────┐
│ Metric                 │ Before  │ After   │ Improvement         │
├────────────────────────────────────────────────────────────────────┤
│ Dev Build Time         │ 45s     │ 8s      │ -82% 🚀            │
│ Prod Build Time        │ 204s    │ 47s     │ -77% 🚀            │
│ Hot Reload             │ 3.2s    │ 0.4s    │ -88% 🚀            │
│ Bundle Size            │ 1.8MB   │ 489KB   │ -73% 🚀            │
│ Cache Hit Rate         │ 0%      │ 92%     │ +92% 🚀            │
└────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════
  COMMANDS
════════════════════════════════════════════════════════════════════════

• `/webpack-config` - Full webpack analysis
• `/webpack-config --speed` - Build speed optimization
• `/webpack-config --size` - Bundle size optimization
• `/webpack-config --analyze` - Bundle composition analysis
• `/webpack-config --generate` - Generate optimized config
• `/webpack-config --cache` - Cache configuration

════════════════════════════════════════════════════════════════════════

**SENA 🦁 Webpack Config** - Blazing fast builds, tiny bundles