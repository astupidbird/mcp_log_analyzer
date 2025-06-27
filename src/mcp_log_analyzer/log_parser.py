#!/usr/bin/env python3
"""
日志解析器类
"""

from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass

@dataclass
class LogEntry:
    """日志条目数据结构"""
    request_time: str
    request_duration: str
    attack_type: str
    intercept_status: str
    client_ip: str
    proxy_ip: str
    domain: str
    url: str
    request_method: str
    referer: str
    cache_status: str
    status_code: str
    page_size: str
    user_agent: str
    raw_line: str

class LogParser:
    """日志解析器"""
    
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        
    def parse_line(self, line: str) -> Optional[LogEntry]:
        """解析单行日志"""
        if not line.strip() or line.startswith('#'):
            return None
            
        # 替换<SP>为实际空格
        line = line.replace('<SP>', ' ')
        
        # 移除开头的"-"预留字段
        if line.startswith('- '):
            line = line[2:]
        
        try:
            parts = line.split(' ')
            if len(parts) < 14:
                return None
                
            return LogEntry(
                request_time=parts[0] + ' ' + parts[1],
                request_duration=parts[2],
                attack_type=parts[3],
                intercept_status=parts[4],
                client_ip=parts[5],
                proxy_ip=parts[6],
                domain=parts[7],
                url=parts[8],
                request_method=parts[9],
                referer=parts[10],
                cache_status=parts[11],
                status_code=parts[12],
                page_size=parts[13],
                user_agent=' '.join(parts[14:]) if len(parts) > 14 else parts[13],
                raw_line=line
            )
        except Exception as e:
            print(f"解析行时出错: {e}")
            return None
    
    def read_lines(self, start_line: int = 0, count: int = 10) -> List[LogEntry]:
        """读取指定范围的日志行"""
        entries = []
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
            # 如果count为None，读取从start_line开始的所有行
            if count is None:
                target_lines = lines[start_line:]
            else:
                target_lines = lines[start_line:start_line + count]
                
            for line in target_lines:
                entry = self.parse_line(line.strip())
                if entry:
                    entries.append(entry)
                    
        except Exception as e:
            print(f"读取文件时出错: {e}")
            
        return entries
    
    def search_logs(self, keyword: str, max_results: int = 100) -> List[LogEntry]:
        """搜索包含关键词的日志条目"""
        entries = []
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                count = 0
                for line in f:
                    if count >= max_results:
                        break
                    if keyword.lower() in line.lower():
                        entry = self.parse_line(line.strip())
                        if entry:
                            entries.append(entry)
                            count += 1
        except Exception as e:
            print(f"搜索日志时出错: {e}")
            
        return entries
    
    def get_file_info(self) -> Dict[str, Any]:
        """获取文件信息"""
        try:
            stat = self.file_path.stat()
            with open(self.file_path, 'r', encoding='utf-8') as f:
                line_count = sum(1 for _ in f)
            
            return {
                "file_path": str(self.file_path),
                "file_size": stat.st_size,
                "line_count": line_count,
                "last_modified": datetime.fromtimestamp(stat.st_mtime).isoformat()
            }
        except Exception as e:
            return {"error": f"获取文件信息时出错: {e}"}