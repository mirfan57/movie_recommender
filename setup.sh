mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enablCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml