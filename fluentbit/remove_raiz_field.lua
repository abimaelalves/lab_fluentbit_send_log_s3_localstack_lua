-- Remove o campo da raiz json
function remove_raiz_field(tag, timestamp, record)
    -- Remove o campo 'dd.span_id' da raiz do json
    record["dd.span_id"] = nil
    return 1, timestamp, record
end