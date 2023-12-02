#include <stdio.h>
#include <stdlib.h>

#define RED 12
#define GREEN 13
#define BLUE 14

int p1(FILE *, int);

size_t strLen(char *);
void strAppend(char *, char);

int getFileNumOfLines(FILE *);
char **getFileLines(FILE *, const int, const int);
int getMaxLineLength(FILE *);
void free2DChar(char **, const int);
char **strToWords(char *);

int main(void)
{
	FILE *fp = fopen("test_input_1.txt", "r");

	const int MAX_LINE_LENGTH = getMaxLineLength(fp);

	if(fp == NULL)
	{
		perror("Cannot open input file!");
		return -1;
	}

	p1(fp, MAX_LINE_LENGTH);

	fclose(fp);

	return 0;
}

size_t strLen(char *str)
{
	size_t len;
	for(len = 0; str[len] != '\0'; len++);

	return len;
}

void strAppend(char *str, char c)
{
	int len = (int)strLen(str);

	str[len] = c;
	str[len + 1] = '\0';
}

void free2DChar(char **arr, const int rows)
{
	for(int i = 0; i < rows; i++)
	{
		free(arr[i]);
	}

	free(arr);
}

int getFileNumOfLines(FILE *fp)
{
	rewind(fp);

	int lines = 0;
	char ch;

	while((ch = fgetc(fp)) != EOF)
	{
		if(ch == '\n')
		{
			lines++;
		}
	}

	return lines;
}

int getMaxLineLength(FILE *fp)
{
	rewind(fp);

	char ch;
	int max_line_length = 0;
	int tmp_line_length = 0;

	while((ch = fgetc(fp)) != EOF)
	{
		tmp_line_length++;

		if(ch == '\n')
		{
			if(tmp_line_length > max_line_length)
			{
				max_line_length = tmp_line_length;
			}

			tmp_line_length = 0;
		}
	}

	return max_line_length;
}

char **getFileLines(FILE *fp, const int lines, const int MAX_LINE_LENGTH)
{
	rewind(fp);

	char **contents = (char **)malloc(lines * sizeof(char *));
	char ch;

	rewind(fp);

	for(int i = 0; i < lines; i++)
	{
		contents[i] = (char *)malloc((MAX_LINE_LENGTH + 1) * sizeof(char));
		/* handle allocation fail */

		for(int x = 0; i < lines; x++)
		{
			if((ch = fgetc(fp)) == '\n')
			{
				contents[i][x] = '\0';
				break;
			}

			contents[i][x] = ch;
		}
	}

	return contents;
}

char **strToWords(char *str)
{
	int len = (int)strLen(str);

	char **words = (char **)malloc((len + 1) * sizeof(char *));
	/* check for allocation fail */
	char tmp[len];

	int x = 0;
	for(int i = 0; i < len; i++)
	{
		if(str[i] == ' ')
		{
			printf("%s\n", tmp);
			words[x] = (char *)malloc((strLen(tmp) + 1) * sizeof(char));
			words[x] = tmp;
			x++;

			for(int j = 0; j < len; j++)
			{
				tmp[j] = '\0';
			}

			continue;
		}

		strAppend(tmp, str[i]);
	}

	return words;
}

int p1(FILE *fp, const int MAX_LINE_LENGTH)
{
	int sum_of_ids = 0;
	const int lines = getFileNumOfLines(fp);
	char **contents = getFileLines(fp, lines, MAX_LINE_LENGTH);

	for(int i = 0; i < lines; i++)
	{
		printf("%ld - ", strLen(contents[i]));
		printf("%s\n", contents[i]);
	}

	char **words = strToWords(contents[0]);

	free2DChar(words, (int)strLen(contents[0]));

	rewind(fp);

	free2DChar(contents, lines);

	return sum_of_ids;
}
