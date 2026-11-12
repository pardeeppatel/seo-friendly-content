#!/usr/bin/env node
/**
 * SEO Friendly Content Skill Installer, Updater & CLI
 * Developed by Pardeep Kumar (ToolNPlay.com)
 */
const fs = require("fs");
const path = require("path");
const { spawn } = require("child_process");

const args = process.argv.slice(2);
const SKILL_NAME = "seo-friendly-content";

function showHelp() {
  console.log(`
SEO Friendly Content v1.0.0 — Interactive On-Page SEO & Human-Writing Skill
  Developed by Pardeep Kumar | Powered by ToolNPlay.com (https://ToolNPlay.com)
  GitHub: https://github.com/PardeepPatel/seo-friendly-content

Usage:
  npx github:pardeeppatel/seo-friendly-content [options]

Options:
  --global, -g     Install globally to ~/.gemini/config/skills/${SKILL_NAME}
  --update, -u     Update existing installations to the latest version
  --cursor         Install to .cursor/skills/${SKILL_NAME}
  --claude         Install to .claude/skills/${SKILL_NAME}
  --gemini         Install to .agents/skills/${SKILL_NAME} and ~/.gemini/config/skills/${SKILL_NAME}
  --agents         Install to .agents/skills/${SKILL_NAME} (default workspace install)
  --audit          Pass remaining flags to scripts/audit_seo_content.py
  --help, -h       Show this help message
`);
}

if (args.includes("--help") || args.includes("-h")) {
  showHelp();
  process.exit(0);
}

if (args.includes("--audit")) {
  const scriptPath = path.join(__dirname, "..", "skill", "scripts", "audit_seo_content.py");
  const passthrough = args.filter((a) => a !== "--audit");
  const child = spawn("python3", [scriptPath, ...passthrough], { stdio: "inherit" });
  child.on("exit", (code) => process.exit(code || 0));
} else {
  const homeDir = process.env.HOME || process.env.USERPROFILE;
  const targets = [];
  const isUpdate = args.includes("--update") || args.includes("-u");

  if (args.includes("--global") || args.includes("-g") || isUpdate) {
    targets.push(path.join(homeDir, ".gemini", "config", "skills", SKILL_NAME));
    targets.push(path.join(homeDir, ".gemini", "antigravity", "skills", SKILL_NAME));

    const localAgents = path.join(process.cwd(), ".agents", "skills", SKILL_NAME);
    const localCursor = path.join(process.cwd(), ".cursor", "skills", SKILL_NAME);
    const localClaude = path.join(process.cwd(), ".claude", "skills", SKILL_NAME);
    if (fs.existsSync(localAgents)) targets.push(localAgents);
    if (fs.existsSync(localCursor)) targets.push(localCursor);
    if (fs.existsSync(localClaude)) targets.push(localClaude);
  } else if (args.includes("--cursor")) {
    targets.push(path.join(process.cwd(), ".cursor", "skills", SKILL_NAME));
  } else if (args.includes("--claude")) {
    targets.push(path.join(process.cwd(), ".claude", "skills", SKILL_NAME));
  } else if (args.includes("--gemini")) {
    targets.push(path.join(process.cwd(), ".agents", "skills", SKILL_NAME));
    targets.push(path.join(homeDir, ".gemini", "config", "skills", SKILL_NAME));
  } else {
    targets.push(path.join(process.cwd(), ".agents", "skills", SKILL_NAME));
  }

  const sourceSkill = path.join(__dirname, "..", "skill");
  const actionWord = isUpdate ? "updated" : "installed";

  console.log(`\nSEO Friendly Content v1.0.0 (Developed by Pardeep Kumar | ToolNPlay.com) ${actionWord} to:`);
  for (const targetBase of targets) {
    fs.mkdirSync(targetBase, { recursive: true });
    fs.cpSync(sourceSkill, targetBase, { recursive: true, force: true });
    console.log(`  - ${targetBase}`);
  }
  console.log(`\nReady! Ask your AI assistant: "Write an SEO article using seo-friendly-content"\n`);
}
