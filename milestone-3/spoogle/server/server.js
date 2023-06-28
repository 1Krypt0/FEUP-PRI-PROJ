import cors from "cors";
import express from "express";

const BASE_URL = "http://localhost:8983/solr/articles/select?";
const MLT_BASE_URL = "http://localhost:8983/solr/articles/mlt?";

async function fetchSolr(baseUrl, params) {
  const url = baseUrl + new URLSearchParams(params);
  const fetchResult = await fetch(url, {
    method: "GET",
    headers: {
      "Access-Control-Allow-Methods": "GET",
      "Access-Control-Allow-Headers": "Content-Type",
      "Access-Control-Allow-Credentials": true,
    },
  })
    .then((result) => result.json())
    .then((data) => {
      return {
        docs: data.response.docs,
        numFound: data.response.numFound,
      };
    });

  return fetchResult;
}

const app = express();
app.use(cors());

const port = 3000;

app.get("/article/:id", async (req, res) => {
  const id = req.params.id;
  const query = `id:${id}`;
  const params = {
    "q.op": "OR",
    rows: 1,
    wt: "json",
    q: query,
  };
  const results = await fetchSolr(BASE_URL, params);
  const article = results.docs[0];
  res.send(article);
});

app.get("/search", async (req, res) => {
  const params = {
    q: req.query.q,
    "q.op": "AND",
    qf: "title^10 content^5 tags^3 sections^3 author",
    wt: "json",
    defType: "edismax",
    rows: 10,
    start: req.query.page * 10,
  };
  const results = await fetchSolr(BASE_URL, params);
  res.send(results);
});

app.get("/mlt", async (req, res) => {
  const params = {
    defType: "edismax",
    wt: "json",
    "q.op": "OR",
    q: "id:" + req.query.id,
    qf: "title^10 content^5 tags^3 sections^3 author date id",
    rows: 10,
    start: req.query.page * 10,
  };
  const results = await fetchSolr(MLT_BASE_URL, params);
  res.send(results);
});

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});
