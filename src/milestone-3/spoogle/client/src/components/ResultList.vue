<script setup lang="ts">
import ResultCard from "./ResultCard.vue";
export interface Article {
  id: string;
  title: string;
  url: string;
  content: string;
  author: string;
  date: Date;
  tags: string[];
  sections: string[];
}

export interface Results {
  results: Article[];
}

const props = defineProps<Results>();
</script>

<template>
  <div class="w-full flex flex-col gap-10">
    <ResultCard
      v-for="article of results"
      :key="article.id"
      :id="article.id"
      :title="article.title"
      :url="article.url"
      :content="article.content"
      :author="article.author"
      :tags="article.tags"
      :sections="article.sections"
      :date="
        article.date.toLocaleDateString(undefined, {
          year: 'numeric',
          month: 'long',
          day: 'numeric',
        })
      "
    />
  </div>
</template>
