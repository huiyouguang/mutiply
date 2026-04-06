import os
import re

REMOVE_KEYS = [
    'rate', 'aliases', 'TQ_explain', 'TQ_extra_instructions', 'TQ_short_mode',
    'TQ_show_backlink', 'TQ_show_cancelled_date', 'TQ_show_created_date', 'TQ_show_depends_on',
    'TQ_show_done_date', 'TQ_show_due_date', 'TQ_show_edit_button', 'TQ_show_tags',
    'TQ_show_task_count', 'TQ_show_tree', 'TQ_show_urgency',
    '笔记ID', '分数', '章节号', 'banner', 'UID', '参考资料:', '科目:', '理解程度:',
    '难度等级:', '学习时间:', '知识点:', 'alias', 'cdate', 'Cover', 'cssclass', 'mindmap', 'point'
]

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if match:
        frontmatter = match.group(1)
        lines = frontmatter.split('\n')
        new_lines = []
        for line in lines:
            if ':' in line:
                key = line.split(':', 1)[0].strip()
                if key not in REMOVE_KEYS:
                    new_lines.append(line)
            else:
                new_lines.append(line)
        if new_lines:
            new_frontmatter = '---\n' + '\n'.join(new_lines) + '\n---\n'
            new_content = re.sub(r'^---\n(.*?)\n---\n', new_frontmatter, content, flags=re.DOTALL)
        else:
            new_content = re.sub(r'^---\n(.*?)\n---\n', '', content, flags=re.DOTALL)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"已移除指定属性: {filepath}")