### Polisci-ish

This is a tool to enhance political science research labs by providing a dashboard with terrible abstract summaries from APSR articles. It should in now way or form be used to communicate political science research results or act as replacement for reading the original articles or abstracts.

This work has significantly improved working conditions (and satisfaction) of student research assistants at the Institute for Political Science, University of Hannover, Germany. 

**Abstract transformation**

For transforming the abstracts into something mildly entertaining, the transformer (ha, ha, ha...) model mistral 7b is used.

**Dashboard**

The dashboard is built using [nicegui](https://nicegui.io/) to enable easy deployment on locally or, if necessary, on the web. Dashboard requires pre-computed transformed abstracts to avoid computation cost. The dashboard updates twice daily. In the morning at 7am and during lunch, at 12:35pm. 