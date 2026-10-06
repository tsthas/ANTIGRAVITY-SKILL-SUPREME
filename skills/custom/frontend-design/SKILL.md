---
name: frontend-design
description: >-
  Diretrizes de design e padrões visuais de alta qualidade (UI/UX) para interfaces Web e Mobile (React Native / Expo).
  Ative esta skill ao criar, refatorar ou estilizar telas, componentes de interface, layouts, temas (dark/light mode),
  paletas de cores, tipografia, micro-interações e animações.
---

# Skill: Frontend & Mobile Design System (UI/UX de Alta Fidelidade)

Esta skill orienta o desenvolvimento de interfaces de usuário com acabamento profissional, estética moderna e usabilidade refinada, eliminando o visual genérico ("IA template") e garantindo consistência entre Web e Mobile (Android/React Native).

---

## 🎨 1. FILOSOFIA DE DESIGN: ADEUS AO "VISUAL GENÉRICO DE IA"

Evite padrões cansados e genéricos (ex: fundo cinza claro `#f3f4f6`, botões azuis puros `#007bff`, cantos excessivamente arredondados sem contraste ou sombras duras).

### Pilares Visuais:
1. **Intencionalidade e Densidade:** Interfaces profissionais têm hierarquia clara. Menos caixas aninhadas desnecessárias, mais espaçamento consistente e contraste tipográfico.
2. **Paletas Curadas (HSL/Tokens Semânticos):**
   * Cores de destaque (Primary/Accent) com tonalidades ricas e saturadas com elegância (ex: Slate, Indigo profundo, Violeta sofisticado, Emerald ou Amber em vez de cores primárias puras).
   * **Modo Escuro (Dark Mode) Nativo:** Use superfícies em camadas (Layering: base `#09090b` ou `#0f172a`, card `#18181b` ou `#1e293b`, hover `#27272a`), nunca preto absoluto `#000000` em tudo sem profundidade.
3. **Tipografia com Personalidade:**
   * Abandone fontes de sistema genéricas. Adote tipografias modernas: **Inter**, **Plus Jakarta Sans**, **Outfit**, **Geist** ou **Roboto**.
   * Diferencie claramente títulos com peso semibold/bold e entrelinha balanceada (`tracking-tight`), e corpo de texto com leitura confortável.

---

## 📐 2. SISTEMA DE DESIGN TOKENS (WEB & MOBILE)

Tanto na Web (CSS Variables / Tailwind) quanto no Mobile (StyleSheet / React Native / Unistyles), estruture o design em tokens semânticos:

### Estrutura de Cores Semânticas
```json
{
  "bg-primary": "Superfície principal de fundo",
  "bg-surface": "Fundo de cards e modais elevados",
  "bg-muted": "Fundo secundário para inputs ou áreas secundárias",
  "text-primary": "Texto principal de alto contraste (ex: 90% a 95% de luminosidade no dark mode)",
  "text-secondary": "Texto de apoio ou rótulos (60% a 70% de luminosidade)",
  "border-subtle": "Bordas finas com baixa opacidade para separação sutil (ex: rgba(255,255,255,0.08))",
  "accent": "Cor de ação principal (botões primários, badges de destaque)",
  "accent-hover": "Variação de luminosidade para estado ativo/hover"
}
```

---

## ✨ 3. MICRO-INTERAÇÕES & ESTADOS DE COMPONENTES

Uma interface profissional parece "viva" e responde ao toque ou cursor do usuário:

### Estados Obrigatórios para Todo Elemento Interativo:
* **Default:** Estado de repouso equilibrado.
* **Hover / Press:** Feedback tátil ou visual imediato (leve clareamento de fundo, escala sutil `scale(0.98)` em botões no clique).
* **Focus-Visible:** Anel de foco acessível para navegação via teclado (`ring-2 ring-accent/50 outline-none`).
* **Disabled:** Redução de opacidade e remoção de eventos do cursor/toque sem quebrar o layout.
* **Loading / Skeletons:** Nunca deixe a tela vazia ou travada. Utilize skeletons com efeito shimmer/pulso animado com o mesmo formato do conteúdo final.

---

## 📱 4. DIRETRIZES ESPECÍFICAS PARA ANDROID / REACT NATIVE (EXPO)

Ao projetar para dispositivos móveis:

1. **Touch Targets Confortáveis:**
   * Elementos clicáveis (botões, ícones, itens de lista) devem ter no mínimo **48x48 dp** de área de toque real (use `hitSlop` se o ícone for menor).
2. **Respeito à Safe Area:**
   * Sempre considerar barra de status, entalhes de câmera (Notch / Dynamic Island) e barra de gestos inferior com `react-native-safe-area-context`.
3. **Feedback Háptico:**
   * Em ações críticas (concluir tarefa, erro de validação, clique em botões principais), utilize feedback tátil (`expo-haptics`).
4. **Navegação Fluida:**
   * Transições nativas de tela usando React Navigation ou Expo Router, respeitando a animação padrão do Android (slide/fade).

---

## 📋 5. CHECKLIST DE ENTREGA DE INTERFACE

Antes de considerar qualquer componente ou tela concluído:
- [ ] O contraste de texto atende a acessibilidade WCAG AA (mínimo 4.5:1 para texto normal).
- [ ] O layout é responsivo (testado em viewport desktop e mobile 360-412px).
- [ ] Não há "saltos" visuais durante o carregamento de dados (layouts preservados com skeletons).
- [ ] Estados vazios (*empty states*) contam com mensagem amigável, ícone ilustrativo e chamada para ação clara.
- [ ] Formulários possuem validação em tempo real com mensagens de erro claras abaixo dos campos.
