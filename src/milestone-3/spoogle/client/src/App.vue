<script setup lang="ts">
import TheHeader from "./components/TheHeader.vue";
import TheFooter from "./components/TheFooter.vue";
import { provide, ref, watch } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";

const route = useRoute();
const isHome = ref(true);

const api = axios.create({
  baseURL: "http://localhost:3000",
  timeout: 2000,
});
provide("api", api);

const update = ref(0);

watch(
  () => route.fullPath,
  async (newRoute) => {
    if (newRoute === "/") {
      isHome.value = true;
    } else {
      isHome.value = false;
    }
    update.value++;
  }
);
</script>

<template>
  <div id="wrapper" class="min-h-full grid">
    <TheHeader v-if="!isHome" />
    <div v-else></div>

    <RouterView :key="update" />

    <TheFooter />
  </div>
</template>
