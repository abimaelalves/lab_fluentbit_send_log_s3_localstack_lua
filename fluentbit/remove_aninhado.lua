-- Remove o campo aninhados
function remove_aninhado(tag, timestamp, record)
    -- Remove o campo aninhados exemplo: communication.request.headers.X-Real-IP
    if record["communication"] and record["communication"]["request"] and record["communication"]["request"]["headers"] then
        record["communication"]["request"]["headers"]["X-Real-IP"] = nil
    end
    -- Remove o campo aninhados exemplo: communication.request.headers.cache-control
    if record["communication"] and record["communication"]["response"] and record["communication"]["response"]["headers"] then
        record["communication"]["response"]["headers"]["cache-control"] = nil
    end
    return 1, timestamp, record
end