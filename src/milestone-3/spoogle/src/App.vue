<script setup lang="ts">
import TheHeader from "./components/TheHeader.vue";
import TheFooter from "./components/TheFooter.vue";
</script>

<template>
  <div id="wrapper" class="min-h-full grid">
    <TheHeader />

    <RouterView />

    <TheFooter />
  </div>
</template>
