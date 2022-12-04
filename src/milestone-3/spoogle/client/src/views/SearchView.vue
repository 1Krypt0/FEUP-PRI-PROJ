<script setup lang="ts">
import { onBeforeMount, ref } from "vue";
import { useRoute } from "vue-router";
import ResultList from "../components/ResultList.vue";
import FilterBox from "../components/FilterBox.vue";

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

const getItems = (query: string) => {
  results.value = [
    {
      id: "789b8820-b4ce-4548-9af9-845c11e6353b",
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
      date: new Date(),
      tags: ["astrocast", " hiber"],
      sections: ["europe"],
    },
    {
      id: "1",
      title: "Fancy title 1",
      content: "Fancy content of the very lengthy news article 1",
      url: "Url 1",
      author: "Author 1",
      date: new Date(),
      tags: ["tag 0", "tag1"],
      sections: ["section0", "section1"],
    },
    {
      id: "2",
      title: "Fancy title 2",
      content: "Fancy content of the very lengthy news article 2",
      url: "Url 2",
      author: "Author 2",
      date: new Date(),
      tags: ["tag 0", "tag1"],
      sections: ["section0", "section1"],
    },
    {
      id: "3",
      title: "Fancy title 3",
      content: "Fancy content of the very lengthy news article 3",
      url: "Url 3",
      author: "Author 0",
      date: new Date(),
      tags: ["tag 0", "tag1"],
      sections: ["section0", "section1"],
    },
  ];
};

const results = ref([
  {
    id: "",
    title: "",
    url: "",
    content: "",
    author: "",
    date: new Date(),
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
