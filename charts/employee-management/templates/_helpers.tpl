{{- define "employee-management.labels" -}}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/environment: {{ .Values.global.environment }}
{{- end }}

{{- define "employee-management.selectorLabels" -}}
app: {{ .Chart.Name }}-{{ .Release.Name }}
{{- end }}

