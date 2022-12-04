<script setup lang="ts">
import { inject, onMounted, ref } from "vue";
import ResultTagSection from "../components/ResultTagSection.vue";
import type { AxiosInstance } from "axios";
export interface Article {
  id: string;
}

const api = inject("api") as AxiosInstance;
const props = defineProps<Article>();

const getItem = (id: string) => {
  api
    .get(`/article/${id}`)
    .then((response) => {
      article.value = response.data;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
};

const article = ref({
  title: "",
  content: "",
  url: "",
  author: "",
  date: "",
  tags: [""],
  sections: [""],
});

// use id to fetch the article before mounting the page
onMounted(() => getItem(props.id));
</script>

<template>
  <main class="w-2/4 mx-auto flex flex-col">
    <h1 class="text-5xl font-sn font-bold pt-20">{{ article.title }}</h1>
    <section>
      <p class="pb-3">{{ article.author }} - {{ article.date }}</p>

      <ResultTagSection
        v-for="tag of article.tags"
        :key="tag"
        :content="tag"
        :is-tag="true"
      />
      <ResultTagSection
        v-for="section of article.sections"
        :key="section"
        :content="section"
        :is-tag="false"
      />
    </section>
    <p class="text-lg pt-10">{{ article.content }}</p>
  </main>
</template>
