module.exports = {
  chainWebpack: config => {
    config.plugin('html').tap(args => {
      args[0].title = 'API Example'
      return args
    })
  },
  devServer: {
    host: '0.0.0.0',
    port: '8080'
  }
}
