const express = require("express");
const cors = require("cors");
const axios = require("axios");

const BASE_URL = "http://localhost:8983/solr/articles/select";
const MLT_BASE_URL = "http://localhost:8983/solr/articles/mlt";

const solr = axios.create({
  baseURL: BASE_URL,
  timeout: 10000,
});

const solrMlt = axios.create({
  baseURL: MLT_BASE_URL,
  timeout: 10000,
})

async function searchSolr(query, page) {
  const response = await solr.get(BASE_URL, {
    params: {
      defType: "edismax",
      indent: true,
      "q.op": "AND",
      qf: "title^10 content^5 tags^3 sections^3 author date id",
      rows: 8,
      start: page * 8,
      q: query,
    },
  });

  const solrResponse = response.data.response;

  if (solrResponse) {
    const docs = solrResponse.docs;
    const numFound = solrResponse.numFound;
    console.log("Found a total of", numFound);
    return {
      docs,
      numFound,
    };
  }
}

async function mltSolr(id, page) {

  // console.log("page is ", page);

  // http://localhost:8983/solr/articles/mlt?q=id%3A7e8fff96-96a6-4482-8427-737ee27d70dd
  let url = "http://localhost:8983/solr/articles/mlt?q=id%3A" + id;
  console.log(url);
  console.log("start is", page * 8);
  // console.log(page);
  const response = await solrMlt.get(MLT_BASE_URL + '?q=id%3A' + id, {
    params: {
      rows: 8,
      start: page * 8,
      "mlt.match.include": false,
    }
  });

  const solrResponse = response.data.response;
  console.log(solrResponse);
  // console.log("sr " + solrResponse.docs);
  if (solrResponse) {
    const docs = solrResponse.docs;
    const numFound = solrResponse.numFound;
    console.log("Found a total of", numFound);
    return {
      docs,
      numFound,
    };
  }
}

const app = express();
app.use(cors());

const port = 3000;

app.get("/article/:id", async (req, res) => {
  const id = req.params.id;
  const query = `id:${id}`;
  const results = await searchSolr(query, 0);
  const article = results.docs[0];
  res.send(article);
});

app.get("/search", async (req, res) => {
  const results = await searchSolr(req.query.q, req.query.page);
  res.send(results);
});

app.get("/mlt", async (req, res) => {
  const results = await mltSolr(req.query.id, req.query.page);
  res.send(results);
});

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});
