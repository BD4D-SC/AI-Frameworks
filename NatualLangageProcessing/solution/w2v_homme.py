token="homme"
token_stem = stemmer.stem(token)

columns = ["CBOW", "skip-gram", "pretrained"]
df_ = []
msw_cbow = model_cbow.wv.most_similar([token_stem])
df_.append([msw_cbow[k][0] for k in range(10)])
msw_sg = model_sg.wv.most_similar([token_stem])
df_.append([msw_sg[k][0] for k in range(10)])
msw_pretrained = model_pretrained.wv.most_similar([token])
df_.append([msw_pretrained[k][0] for k in range(10)])
pd.DataFrame(np.array(df_).T, columns=columns)