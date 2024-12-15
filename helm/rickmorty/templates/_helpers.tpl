{{- define "rickmorty.name" -}}
{{ .Chart.Name }}
{{- end -}}

{{- define "rickmorty.fullname" -}}
{{ .Release.Name }}-{{ .Chart.Name }}
{{- end -}}

{{- define "rickmorty.labels" -}}
app.kubernetes.io/name: {{ include "rickmorty.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}
