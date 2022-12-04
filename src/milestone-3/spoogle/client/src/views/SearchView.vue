<script setup lang="ts">
import { inject, onBeforeMount, ref } from "vue";
import { useRoute } from "vue-router";
import ResultList from "../components/ResultList.vue";
import FilterBox from "../components/FilterBox.vue";
import type { AxiosInstance } from "axios";

export interface Article {
  id: string;
  title: string;
  url: string;
  content: string;
  author: string;
  date: string;
  tags: string[];
  sections: string[];
}

export interface Results {
  results: Article[];
}

const api = inject("api") as AxiosInstance;
const getItems = (query: string) => {
  api
    .get("/search", {
      params: {
        q: query,
      },
    })
    .then((response) => {
      results.value = response.data;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
};

const results = ref([
  {
    id: "",
    title: "",
    url: "",
    content: "",
    author: "",
    date: "",
    tags: [""],
    sections: [""],
  },
]);
const query = useRoute().query.q as string;

onBeforeMount(() => {
  getItems(query);
});
</script>

<template>
  <div class="flex pt-20">
    <section class="flex w-1/5 flex-col px-10">
      <h2 class="text-3xl font-sn pb-10">Filters</h2>
      <FilterBox />
    </section>
    <main class="flex w-3/5 justify-center px-10">
      <ResultList :results="results" />
    </main>
    <section class="flex w-1/5 flex-col"></section>
  </div>
</template>
