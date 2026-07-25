# metadata.json (required fields)

```json
{
  "title": "Lec …",
  "video_id": "…",
  "url": "https://www.youtube.com/watch?v=…",
  "duration_seconds": 0,
  "channel": "…",
  "instructor": "…",
  "playlist_index": 0,
  "skill": "youtube-lecture-tutor",
  "content_type": "theory_concept",
  "topic_count": 8,
  "package_variant": "educative-spine-v3",
  "requires_claim_mining": true,
  "topics": ["short", "list", "of", "topic", "titles"]
}
```

`content_type` must be one of:  
`math_technical` | `code_tutorial` | `tool_product` | `theory_concept` | `research_review` | `soft_skills` | `mixed`

Set `requires_claim_mining` to `true` for every new package. The validator then requires
`raw/claims/topic-NN.md` for every NOTES topic and `raw/coverage-checklist.md`. Omit the
field only for an older package that is being checked without a claim-mining retrofit.
