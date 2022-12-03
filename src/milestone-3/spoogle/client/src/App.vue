<script setup lang="ts">
import TheHeader from "./components/TheHeader.vue";
import TheFooter from "./components/TheFooter.vue";
import { ref, watch } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const isHome = ref(true);

watch(
  () => route.fullPath,
  async (newRoute) => {
    if (newRoute === "/") {
      isHome.value = true;
    } else {
      isHome.value = false;
    }
  }
);
</script>

<template>
  <div id="wrapper" class="min-h-full grid">
    <TheHeader v-if="!isHome" />
    <div v-else></div>

    <RouterView />

    <TheFooter />
  </div>
</template>
