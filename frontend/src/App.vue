<template>
  <div style="padding: 20px; font-family: Arial;">
    <h1>Vue + Django + Docker</h1>

    <button @click="probarApi">Probar API Django</button>
    <p>{{ mensaje }}</p>

    <hr>

    <button @click="probarCache">Probar caché Redis</button>
    <p>{{ mensajeCache }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      mensaje: "",
      mensajeCache: ""
    }
  },
  methods: {
    async probarApi() {
      try {
        const respuesta = await fetch("http://localhost:8000/api/hello/")
        const data = await respuesta.json()
        this.mensaje = data.message
      } catch (error) {
        this.mensaje = "No se pudo conectar con Django."
      }
    },
    async probarCache() {
      try {
        const respuesta = await fetch("http://localhost:8000/api/cache/")
        const data = await respuesta.json()
        this.mensajeCache = "Visitas guardadas en Redis: " + data.visitas_cache
      } catch (error) {
        this.mensajeCache = "No se pudo probar Redis."
      }
    }
  }
}
</script>