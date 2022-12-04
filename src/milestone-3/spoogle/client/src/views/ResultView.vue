<script setup lang="ts">
import { onMounted, ref } from "vue";
import ResultTagSection from "../components/ResultTagSection.vue";
export interface Article {
  id: string;
}

const props = defineProps<Article>();

const getItem = () => {
  article.value = {
    title: "Astrocast buying Hiber to boost funding and expansion plans",
    content:
      "TAMPA, Fla. — Cash-strapped smallsat operator Astrocast announced \
      plans May 30 to buy Dutch connectivity solutions provider Hiber, which \
      scrapped plans for its own constellation last year following failures on\
      its initial satellites.  Switzerland-based Astrocast said the deal would\
      give it spectrum in the Americas to enable its growing constellation for connecting\
      Internet of Things (IoT) devices to operate globally. Astrocast plans to issue new shares\
      to fund the acquisition. Hiber has also agreed to invest around $11 million in Astrocast’s second\
      stock market listing later this year to help the Swiss startup meet near-term funding needs.  Astrocast hopes to raise 60-80 million euros ($64-86 million) by listing shares on the Euronext Growth Paris\
      junior stock market in France. The startup said it needs more funds to expand its constellation of 12 satellites — including two test spacecraft — to 20 before the end of 2022, and to 40 in 2023 to improve\
      coverage.  By 2025, Astrocast aims to be operating 100 satellites in low Earth orbit.  While the first 20 will be three-unit cubesats, Astrocast has said later models could be larger six-unit cubesats. Astrocast\
      became a public company in August when it raised about $42 million by listing shares on Euronext Growth Oslo in Norway. The operator launched commercially in February for regions outside the Americas which, according to Astrocast\
      spokesperson Fatima Vigil-Perez, currently receive services with a typical two-hour latency. However, Astrocast estimated in its May 13 annual financial report that it needs to raise 43 million Swiss Francs ($45 million)\
      in 2022 for expansion plans that would enable it to improve coverage and satellite revisit rates. The company reported a 21.4 million Swiss Franc loss for 2021. Established operators — and other startups that include\
      SpaceX-owned Swarm  — are also seeking a share of a space-based IoT market that typically uses satellites to connect small devices out the reach of terrestrial networks.  Astrocast says its services are focused on connecting\
      customers in industrial markets that include agriculture, maritime and utilities. Hiber also targets industrial customers — particularly those in the oil & gas, mining, logistics and agriculture markets — and provides\
      satellite-connected devices and solutions that enable customers to monitor and track assets in remote locations.  The Dutch company’s business is based on multi-year subscriptions that cover sensors, network hardware, satellite\
      connectivity and a user interface. In October, Hiber  announced a partnership  to use Inmarsat’s satellites for its IoT solutions after giving up on its own constellation. The Dutch company had surrendered a license to operate\
      a network of 24 IoT smallsats just weeks before, blaming technical issues on four initial satellites it had deployed and financial issues.  Astrocast said acquiring Hiber would give the Swiss company access to L-band spectrum for\
      covering the Americas that is part of an agreement with Inmarsat. Astrocast’s satellites already use L-band to provide services. “Our satellites are designed to provide connectivity globally so there’s\
      no need to wait for the launch of future satellites to provide connectivity in the Americas,” Vigil-Perez said. Astrocast plans to buy Hiber with newly issued shares that currently represent a 16.5% stake\
      in Astrocast. The acquisition is dependent on Astrocast completing its Euronext Growth Paris stock market listing.",
    url: "https://spacenews.com/astrocast-buying-hiber-to-boost-funding-and-expansion-plans/",
    author: "Jason Rainbow",
    date: new Date().toLocaleDateString(undefined, {
      year: "numeric",
      month: "long",
      day: "numeric",
    }),
    tags: ["astrocast", " hiber"],
    sections: ["europe"],
  };
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
onMounted(getItem);
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
