<!--Código correspondiente a html, aqui es la parte principal de la aplicación-->
<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<!--Código correspondiente a JavaScript-->
<script>
export default {
  name: 'App'
}
</script>

<!--Código correspondiente al estilo-->
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
