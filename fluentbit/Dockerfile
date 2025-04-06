FROM amazon/aws-for-fluent-bit:stable

COPY fluent-bit.conf /fluentbit/etc/fluent-bit.conf
COPY parsers.conf /fluentbit/etc/parsers.conf
COPY remove_raiz_field.lua /fluentbit/etc/remove_raiz_field.lua
COPY remove_aninhado.lua /fluentbit/etc/remove_aninhado.lua
