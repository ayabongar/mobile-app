const crypto = require('crypto');

module.exports = {
  resolve: {
    fallback: {
      crypto: false,
    },
  },
  plugins: [
    new webpack.ProvidePlugin({
      process: 'process/browser',
    }),
  ],
};
