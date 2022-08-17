from tokenizers.implementations import ByteLevelBPETokenizer
from tokenizers.processors import BertProcessing


tokenizer = ByteLevelBPETokenizer(
    "./models/sampletoken-vocab.json",
    "./models/sampletoken-merges.txt",
)
tokenizer._tokenizer.post_processor = BertProcessing(
    ("</s>", tokenizer.token_to_id("</s>")),
    ("<s>", tokenizer.token_to_id("<s>")),
)
tokenizer.enable_truncation(max_length=512)

print(
    tokenizer.encode("sp:4856 dp:49152 ptcl:6 ipv:4 vln:0 tnnl:0 bi_dur:34 bi_pkt:14 bi_byte:4544 s2d_dur:32 s2d:7 s2d_byte:555 d2s_dur:33 d2s:7 d2s_byte:3989 bi_min_ps:52 bi_mean_ps:324.57 bi_std_ps:516.42 bi_max_ps:1500 s2d_min_ps:52 s2d_mean_ps:79.29 s2d_std_ps:68.73 s2d_max_ps:235 d2s_min_ps:52 d2s_mean_ps:569.86 d2s_std_ps:657.82 d2s_max_ps:1500 bi_min_pi_ms:0 bi_mean_pi_ms:2.62 bi_std_pi_ms:2.26 bi_max_pi_ms:6 s2d_min_pi_ms:1 s2d_mean_pi_ms:5.33 s2d_std_pi_ms:5.5 s2d_max_pi_ms:16 d2s_min_pi_ms:0 d2s_mean_pi_ms:5.5 d2s_std_pi_ms:6.06 d2s_max_pi_ms:16 bi_syn:2 bi_cwr:0 bi_ece:0 bi_urg:0 bi_ack:13 bi_psh:3 bi_rst:0 bi_fin:2 s2d_syn:1 s2d_cwr:0 s2d_ece:0 s2d_urg:0 s2d_ack:6 s2d_psh:1 s2d_rst:0 s2d_fin:1 d2s_syn:1 d2s_cwr:0 d2s_ece:0 d2s_urg:0 d2s_ack:7 d2s_psh:2 d2s_rst:0 d2s_fin:1 app_name:HTTP app_cat:Web req_server_name:192.168.1.223 client_fingerprint:nan server_fingerprint:nan content_type:text/xml")
)

# Encoding(num_tokens=512, attributes=[ids, type_ids, tokens, offsets, attention_mask, special_tokens_mask, overflowing])

