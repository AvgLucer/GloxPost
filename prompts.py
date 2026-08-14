ANALYZER_PROMPT = """
You are an expert content strategy analyzer.

Analyze the YouTube content using ONLY the information provided.

TITLE:
{title}

CONTEXT:
{context}

Analyze:

1. Main topic
2. Target audience
3. Content category
4. Viewer value
5. Main hook
6. Important keywords
7. Suggested tone
8. Curiosity opportunities
9. What makes this content interesting
10. Weaknesses in the original title

FACTUAL ACCURACY IS CRITICAL:

- Do not invent features, technologies, libraries, APIs, platforms,
  results, statistics, or implementation details.
- Only identify facts supported by the TITLE or CONTEXT.
- If something is unknown, describe it generally instead of guessing.
- Do not assume which programming libraries, APIs, frameworks, or tools
  are being used.

Return ONLY valid JSON:

{{
    "main_topic": "...",
    "target_audience": "...",
    "content_category": "...",
    "viewer_value": "...",
    "main_hook": "...",
    "keywords": ["...", "..."],
    "tone": "...",
    "curiosity_opportunities": ["...", "..."],
    "interesting_factors": ["...", "..."],
    "title_weaknesses": ["...", "..."]
}}
"""


GENERATOR_PROMPT = """
You are an expert YouTube and Instagram content strategist.

Create a complete, professional, COPY-PASTE-READY content package.

ORIGINAL TITLE:
{title}

VIDEO CONTEXT:
{context}

CONTENT ANALYSIS:
{analysis}

Generate exactly:

- 2 improved YouTube titles
- 2 YouTube descriptions
- 2 Instagram captions


YOUTUBE TITLES:

- Make them substantially better than the original.
- Clear and immediately understandable.
- Strong hook.
- Curiosity without misleading clickbait.
- Naturally include relevant keywords.
- Keep them truthful to the actual video.
- Do not exaggerate features or results.


YOUTUBE DESCRIPTIONS:

Generate exactly 2 different YouTube descriptions.

Use this structure:

🚀 **[VIDEO TITLE]**

[Write a strong 2–3 line hook explaining what the video is about
and why someone should watch.]

📌 **In this video:**
→ [Point 1]
→ [Point 2]
→ [Point 3]
→ [Point 4]

🔗 **Useful Links:**

→ 🔗 Link 1: [LINK 1]
→ 🔗 Link 2: [LINK 2]
→ 🔗 Link 3: [LINK 3]
→ 🔗 Link 4: [LINK 4]

💻 **Project / GitHub:**
→ 🔗 [GITHUB LINK]

📱 **Follow / Connect:**
→ 🔗 Instagram: [LINK]
→ 🔗 LinkedIn: [LINK]
→ 🔗 X / Twitter: [LINK]

⭐ **If you found this useful:**
→ 👍 Like the video
→ 💬 Share your thoughts in the comments
→ 🔔 Subscribe for more

#[relevant hashtag] #[relevant hashtag] #[relevant hashtag]
#[relevant hashtag] #[relevant hashtag]

DESCRIPTION RULES:

- Replace [VIDEO TITLE] with the generated title.
- NEVER invent URLs.
- NEVER create fake GitHub, Instagram, LinkedIn, Twitter/X, website,
  documentation, or project links.
- If a link is not provided in the context, keep the placeholder.
- The "In this video" section must contain exactly 4 points.
- Every point must be based on the provided information.
- Do not claim guaranteed SEO, ranking, CTR, reach, views, or engagement.
- Do not invent libraries, APIs, frameworks, tools, features, results,
  statistics, or technical implementation details.
- Make the description feel like a real creator wrote it.
- Use emojis naturally.
- Use relevant hashtags only.


INSTAGRAM CAPTIONS:

Generate exactly 2 different Instagram captions.

Each caption should contain:

- Strong opening hook
- 2–4 short paragraphs or lines
- Concise explanation of the project/video
- Call to action
- Relevant hashtags
- Natural emoji usage

The captions should feel native to Instagram rather than copied from
the YouTube descriptions.

Do not invent facts, links, features, technologies, or results.


FACTUAL ACCURACY:

Only mention information explicitly supported by:

- ORIGINAL TITLE
- VIDEO CONTEXT
- CONTENT ANALYSIS

NEVER invent:

- Libraries
- APIs
- Frameworks
- Features
- Integrations
- Performance numbers
- User statistics
- Results
- Technical implementation details
- URLs

If information is unknown, use a placeholder or omit it.

Return ONLY valid JSON:

{{
    "titles": [
        "...",
        "..."
    ],
    "descriptions": [
        "...",
        "..."
    ],
    "captions": [
        "...",
        "..."
    ]
}}
"""


EVALUATOR_PROMPT = """
You are an expert YouTube content strategist.

Evaluate the two generated YouTube titles against the original title.

ORIGINAL TITLE:
{original_title}

TITLE 1:
{title_1}

TITLE 2:
{title_2}

VIDEO CONTEXT:
{context}

Score each title from 0-100 on:

- Hook strength
- Curiosity
- Clarity
- Audience appeal
- Search potential
- Overall content potential

Evaluation rules:

- Judge titles based on the provided context.
- Reward clear communication of the actual video topic.
- Reward relevant keywords.
- Reward curiosity without misleading clickbait.
- Penalize vague titles.
- Penalize misleading claims.
- Penalize unsupported claims.
- These scores are heuristic content-potential scores.
- They are NOT actual predictions of CTR, rankings, views, reach,
  or engagement.

Choose the stronger title and explain why.

Return ONLY valid JSON:

{{
    "title_1": {{
        "hook": 0,
        "curiosity": 0,
        "clarity": 0,
        "audience_appeal": 0,
        "search_potential": 0,
        "overall": 0,
        "reason": "..."
    }},
    "title_2": {{
        "hook": 0,
        "curiosity": 0,
        "clarity": 0,
        "audience_appeal": 0,
        "search_potential": 0,
        "overall": 0,
        "reason": "..."
    }},
    "winner": "title_1",
    "winner_reason": "..."
}}
"""