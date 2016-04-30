Name     : golang-googlecode-go-tools 
Version  : 0
Release  : 5
URL      : https://github.com/golang/tools/archive/6b41c776c8733a36ba4586aa0bfaf5b6878c41d8.tar.gz
Source0  : https://github.com/golang/tools/archive/6b41c776c8733a36ba4586aa0bfaf5b6878c41d8.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
BuildRequires : go
BuildRequires : golang-googlecode-go-net

%description
This subrepository holds the source for various packages and tools that support
the Go programming language.

%prep
%setup -q -n tools-6b41c776c8733a36ba4586aa0bfaf5b6878c41d8

%build

%install
%global gopath /usr/lib/golang
%global library_path golang.org/x/tools
rm -rf %{buildroot}
# Copy all *.go and *.s files
install -d -p %{buildroot}%{gopath}/src/%{library_path}/
for ext in go s src golden template; do
    for file in $(find . -iname "*.$ext") ; do
         install -d -p %{buildroot}%{gopath}/src/%{library_path}/$(dirname $file)
         cp -pav $file %{buildroot}%{gopath}/src/%{library_path}/$file
    done
done

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export GOPATH=%{buildroot}%{gopath}
go test %{library_path}/cmd/benchcmp
go test %{library_path}/cmd/callgraph
go test %{library_path}/cmd/cover
go test %{library_path}/cmd/digraph
go test %{library_path}/cmd/fiximports
go test %{library_path}/cmd/godoc
go test %{library_path}/cmd/stringer
go test %{library_path}/cmd/vet/testdata ||:
go test %{library_path}/cmd/vet/testdata/divergent ||:
go test %{library_path}/cmd/vet/testdata/incomplete ||:
go test %{library_path}/container/intsets/
go test %{library_path}/go/ast/astutil
go test %{library_path}/go/buildutil
go test %{library_path}/go/callgraph/cha
go test %{library_path}/go/callgraph/rta
go test %{library_path}/go/callgraph/static
go test %{library_path}/go/callgraph/cha
go test %{library_path}/go/callgraph/rta
go test %{library_path}/go/callgraph/static
go test %{library_path}/go/exact
go test %{library_path}/go/gccgoimporter ||:
go test %{library_path}/go/gcimporter
go test %{library_path}/go/importer ||:
go test %{library_path}/go/loader ||:
go test %{library_path}/go/pointer
go test %{library_path}/go/ssa/interp
go test %{library_path}/go/ssa/ssautil
go test %{library_path}/go/ssa ||:
go test %{library_path}/go/types ||:
go test %{library_path}/go/types/typeutil
go test %{library_path}/go/vcs ||:
go test %{library_path}/godoc
go test %{library_path}/godoc/dl ||:
go test %{library_path}/godoc/vfs/mapfs
go test %{library_path}/imports
go test %{library_path}/oracle
go test %{library_path}/present
go test %{library_path}/refactor/eg
go test %{library_path}/refactor/importgraph
go test %{library_path}/refactor/rename

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/golang.org/x/tools/benchmark/parse/parse.go
/usr/lib/golang/src/golang.org/x/tools/benchmark/parse/parse_test.go
/usr/lib/golang/src/golang.org/x/tools/blog/atom/atom.go
/usr/lib/golang/src/golang.org/x/tools/blog/blog.go
/usr/lib/golang/src/golang.org/x/tools/cmd/benchcmp/benchcmp.go
/usr/lib/golang/src/golang.org/x/tools/cmd/benchcmp/benchcmp_test.go
/usr/lib/golang/src/golang.org/x/tools/cmd/benchcmp/compare.go
/usr/lib/golang/src/golang.org/x/tools/cmd/benchcmp/compare_test.go
/usr/lib/golang/src/golang.org/x/tools/cmd/benchcmp/doc.go
/usr/lib/golang/src/golang.org/x/tools/cmd/callgraph/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/callgraph/main_test.go
/usr/lib/golang/src/golang.org/x/tools/cmd/callgraph/testdata/src/pkg/pkg.go
/usr/lib/golang/src/golang.org/x/tools/cmd/callgraph/testdata/src/pkg/pkg_test.go
/usr/lib/golang/src/golang.org/x/tools/cmd/cover/cover.go
/usr/lib/golang/src/golang.org/x/tools/cmd/cover/cover_test.go
/usr/lib/golang/src/golang.org/x/tools/cmd/cover/doc.go
/usr/lib/golang/src/golang.org/x/tools/cmd/cover/func.go
/usr/lib/golang/src/golang.org/x/tools/cmd/cover/html.go
/usr/lib/golang/src/golang.org/x/tools/cmd/cover/testdata/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/cover/testdata/test.go
/usr/lib/golang/src/golang.org/x/tools/cmd/digraph/digraph.go
/usr/lib/golang/src/golang.org/x/tools/cmd/digraph/digraph_test.go
/usr/lib/golang/src/golang.org/x/tools/cmd/eg/eg.go
/usr/lib/golang/src/golang.org/x/tools/cmd/fiximports/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/fiximports/main_test.go
/usr/lib/golang/src/golang.org/x/tools/cmd/fiximports/testdata/src/fruit.io/banana/banana.go
/usr/lib/golang/src/golang.org/x/tools/cmd/fiximports/testdata/src/fruit.io/orange/orange.go
/usr/lib/golang/src/golang.org/x/tools/cmd/fiximports/testdata/src/fruit.io/pear/pear.go
/usr/lib/golang/src/golang.org/x/tools/cmd/fiximports/testdata/src/new.com/one/one.go
/usr/lib/golang/src/golang.org/x/tools/cmd/fiximports/testdata/src/old.com/bad/bad.go
/usr/lib/golang/src/golang.org/x/tools/cmd/fiximports/testdata/src/old.com/one/one.go
/usr/lib/golang/src/golang.org/x/tools/cmd/fiximports/testdata/src/titanic.biz/bar/bar.go
/usr/lib/golang/src/golang.org/x/tools/cmd/fiximports/testdata/src/titanic.biz/foo/foo.go
/usr/lib/golang/src/golang.org/x/tools/cmd/godex/doc.go
/usr/lib/golang/src/golang.org/x/tools/cmd/godex/gc.go
/usr/lib/golang/src/golang.org/x/tools/cmd/godex/gccgo.go
/usr/lib/golang/src/golang.org/x/tools/cmd/godex/godex.go
/usr/lib/golang/src/golang.org/x/tools/cmd/godex/print.go
/usr/lib/golang/src/golang.org/x/tools/cmd/godex/source.go
/usr/lib/golang/src/golang.org/x/tools/cmd/godex/writetype.go
/usr/lib/golang/src/golang.org/x/tools/cmd/godoc/appinit.go
/usr/lib/golang/src/golang.org/x/tools/cmd/godoc/blog.go
/usr/lib/golang/src/golang.org/x/tools/cmd/godoc/codewalk.go
/usr/lib/golang/src/golang.org/x/tools/cmd/godoc/dl.go
/usr/lib/golang/src/golang.org/x/tools/cmd/godoc/doc.go
/usr/lib/golang/src/golang.org/x/tools/cmd/godoc/godoc_test.go
/usr/lib/golang/src/golang.org/x/tools/cmd/godoc/handlers.go
/usr/lib/golang/src/golang.org/x/tools/cmd/godoc/index.go
/usr/lib/golang/src/golang.org/x/tools/cmd/godoc/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/godoc/play.go
/usr/lib/golang/src/golang.org/x/tools/cmd/godoc/remotesearch.go
/usr/lib/golang/src/golang.org/x/tools/cmd/godoc/x.go
/usr/lib/golang/src/golang.org/x/tools/cmd/goimports/doc.go
/usr/lib/golang/src/golang.org/x/tools/cmd/goimports/goimports.go
/usr/lib/golang/src/golang.org/x/tools/cmd/gomvpkg/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/gorename/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/gotype/doc.go
/usr/lib/golang/src/golang.org/x/tools/cmd/gotype/gotype.go
/usr/lib/golang/src/golang.org/x/tools/cmd/gotype/gotype14.go
/usr/lib/golang/src/golang.org/x/tools/cmd/html2article/conv.go
/usr/lib/golang/src/golang.org/x/tools/cmd/oracle/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/present/appengine.go
/usr/lib/golang/src/golang.org/x/tools/cmd/present/dir.go
/usr/lib/golang/src/golang.org/x/tools/cmd/present/doc.go
/usr/lib/golang/src/golang.org/x/tools/cmd/present/local.go
/usr/lib/golang/src/golang.org/x/tools/cmd/present/play.go
/usr/lib/golang/src/golang.org/x/tools/cmd/present/play_http.go
/usr/lib/golang/src/golang.org/x/tools/cmd/present/play_socket.go
/usr/lib/golang/src/golang.org/x/tools/cmd/ssadump/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/stress/stress.go
/usr/lib/golang/src/golang.org/x/tools/cmd/stringer/endtoend_test.go
/usr/lib/golang/src/golang.org/x/tools/cmd/stringer/golden_test.go
/usr/lib/golang/src/golang.org/x/tools/cmd/stringer/stringer.go
/usr/lib/golang/src/golang.org/x/tools/cmd/stringer/testdata/cgo.go
/usr/lib/golang/src/golang.org/x/tools/cmd/stringer/testdata/day.go
/usr/lib/golang/src/golang.org/x/tools/cmd/stringer/testdata/gap.go
/usr/lib/golang/src/golang.org/x/tools/cmd/stringer/testdata/num.go
/usr/lib/golang/src/golang.org/x/tools/cmd/stringer/testdata/number.go
/usr/lib/golang/src/golang.org/x/tools/cmd/stringer/testdata/prime.go
/usr/lib/golang/src/golang.org/x/tools/cmd/stringer/testdata/unum.go
/usr/lib/golang/src/golang.org/x/tools/cmd/stringer/testdata/unum2.go
/usr/lib/golang/src/golang.org/x/tools/cmd/stringer/util_test.go
/usr/lib/golang/src/golang.org/x/tools/cmd/tip/godoc.go
/usr/lib/golang/src/golang.org/x/tools/cmd/tip/talks.go
/usr/lib/golang/src/golang.org/x/tools/cmd/tip/tip.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/asmdecl.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/assign.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/atomic.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/bool.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/buildtag.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/composite.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/copylock.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/deadcode.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/doc.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/example.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/method.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/nilfunc.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/print.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/rangeloop.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/shadow.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/shift.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/structtag.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/asm.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/asm1.s
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/asm2.s
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/asm3.s
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/asm4.s
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/assign.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/atomic.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/bool.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/buildtag.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/buildtag_bad.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/composite.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/copylock_func.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/copylock_range.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/deadcode.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/divergent/buf.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/divergent/buf_test.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/examples_test.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/incomplete/examples_test.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/method.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/nilfunc.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/print.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/rangeloop.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/shadow.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/shift.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/structtag.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/tagtest/file1.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/tagtest/file2.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/unsafeptr.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/testdata/unused.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/types.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/unsafeptr.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/unused.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/vet_test.go
/usr/lib/golang/src/golang.org/x/tools/cmd/vet/whitelist/whitelist.go
/usr/lib/golang/src/golang.org/x/tools/container/intsets/sparse.go
/usr/lib/golang/src/golang.org/x/tools/container/intsets/sparse_test.go
/usr/lib/golang/src/golang.org/x/tools/container/intsets/util.go
/usr/lib/golang/src/golang.org/x/tools/container/intsets/util_test.go
/usr/lib/golang/src/golang.org/x/tools/cover/profile.go
/usr/lib/golang/src/golang.org/x/tools/go/ast/astutil/enclosing.go
/usr/lib/golang/src/golang.org/x/tools/go/ast/astutil/enclosing_test.go
/usr/lib/golang/src/golang.org/x/tools/go/ast/astutil/imports.go
/usr/lib/golang/src/golang.org/x/tools/go/ast/astutil/imports_test.go
/usr/lib/golang/src/golang.org/x/tools/go/ast/astutil/util.go
/usr/lib/golang/src/golang.org/x/tools/go/buildutil/allpackages.go
/usr/lib/golang/src/golang.org/x/tools/go/buildutil/allpackages_test.go
/usr/lib/golang/src/golang.org/x/tools/go/buildutil/fakecontext.go
/usr/lib/golang/src/golang.org/x/tools/go/buildutil/tags.go
/usr/lib/golang/src/golang.org/x/tools/go/buildutil/tags_test.go
/usr/lib/golang/src/golang.org/x/tools/go/buildutil/util.go
/usr/lib/golang/src/golang.org/x/tools/go/buildutil/util_test.go
/usr/lib/golang/src/golang.org/x/tools/go/callgraph/callgraph.go
/usr/lib/golang/src/golang.org/x/tools/go/callgraph/cha/cha.go
/usr/lib/golang/src/golang.org/x/tools/go/callgraph/cha/cha_test.go
/usr/lib/golang/src/golang.org/x/tools/go/callgraph/cha/testdata/func.go
/usr/lib/golang/src/golang.org/x/tools/go/callgraph/cha/testdata/iface.go
/usr/lib/golang/src/golang.org/x/tools/go/callgraph/cha/testdata/recv.go
/usr/lib/golang/src/golang.org/x/tools/go/callgraph/rta/rta.go
/usr/lib/golang/src/golang.org/x/tools/go/callgraph/rta/rta_test.go
/usr/lib/golang/src/golang.org/x/tools/go/callgraph/rta/testdata/func.go
/usr/lib/golang/src/golang.org/x/tools/go/callgraph/rta/testdata/iface.go
/usr/lib/golang/src/golang.org/x/tools/go/callgraph/rta/testdata/rtype.go
/usr/lib/golang/src/golang.org/x/tools/go/callgraph/static/static.go
/usr/lib/golang/src/golang.org/x/tools/go/callgraph/static/static_test.go
/usr/lib/golang/src/golang.org/x/tools/go/callgraph/util.go
/usr/lib/golang/src/golang.org/x/tools/go/exact/exact.go
/usr/lib/golang/src/golang.org/x/tools/go/exact/exact_test.go
/usr/lib/golang/src/golang.org/x/tools/go/exact/go13.go
/usr/lib/golang/src/golang.org/x/tools/go/exact/go14.go
/usr/lib/golang/src/golang.org/x/tools/go/gccgoimporter/gccgoinstallation.go
/usr/lib/golang/src/golang.org/x/tools/go/gccgoimporter/gccgoinstallation_test.go
/usr/lib/golang/src/golang.org/x/tools/go/gccgoimporter/importer.go
/usr/lib/golang/src/golang.org/x/tools/go/gccgoimporter/importer_test.go
/usr/lib/golang/src/golang.org/x/tools/go/gccgoimporter/parser.go
/usr/lib/golang/src/golang.org/x/tools/go/gccgoimporter/parser_test.go
/usr/lib/golang/src/golang.org/x/tools/go/gccgoimporter/testdata/complexnums.go
/usr/lib/golang/src/golang.org/x/tools/go/gccgoimporter/testdata/imports.go
/usr/lib/golang/src/golang.org/x/tools/go/gccgoimporter/testdata/pointer.go
/usr/lib/golang/src/golang.org/x/tools/go/gcimporter/exportdata.go
/usr/lib/golang/src/golang.org/x/tools/go/gcimporter/gcimporter.go
/usr/lib/golang/src/golang.org/x/tools/go/gcimporter/gcimporter_test.go
/usr/lib/golang/src/golang.org/x/tools/go/gcimporter/testdata/exports.go
/usr/lib/golang/src/golang.org/x/tools/go/importer/export.go
/usr/lib/golang/src/golang.org/x/tools/go/importer/import.go
/usr/lib/golang/src/golang.org/x/tools/go/importer/import_test.go
/usr/lib/golang/src/golang.org/x/tools/go/importer/predefined.go
/usr/lib/golang/src/golang.org/x/tools/go/loader/cgo.go
/usr/lib/golang/src/golang.org/x/tools/go/loader/doc.go
/usr/lib/golang/src/golang.org/x/tools/go/loader/example14_test.go
/usr/lib/golang/src/golang.org/x/tools/go/loader/example_test.go
/usr/lib/golang/src/golang.org/x/tools/go/loader/loader.go
/usr/lib/golang/src/golang.org/x/tools/go/loader/loader_test.go
/usr/lib/golang/src/golang.org/x/tools/go/loader/stdlib_test.go
/usr/lib/golang/src/golang.org/x/tools/go/loader/testdata/a.go
/usr/lib/golang/src/golang.org/x/tools/go/loader/testdata/b.go
/usr/lib/golang/src/golang.org/x/tools/go/loader/testdata/badpkgdecl.go
/usr/lib/golang/src/golang.org/x/tools/go/loader/util.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/analysis.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/api.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/callgraph.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/constraint.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/doc.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/example_test.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/gen.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/hvn.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/intrinsics.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/labels.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/opt.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/pointer_test.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/print.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/reflect.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/solve.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/stdlib_test.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/testdata/a_test.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/testdata/another.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/testdata/arrayreflect.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/testdata/arrays.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/testdata/channels.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/testdata/chanreflect.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/testdata/chanreflect1.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/testdata/context.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/testdata/conv.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/testdata/finalizer.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/testdata/flow.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/testdata/fmtexcerpt.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/testdata/func.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/testdata/funcreflect.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/testdata/hello.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/testdata/interfaces.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/testdata/issue9002.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/testdata/mapreflect.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/testdata/maps.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/testdata/panic.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/testdata/recur.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/testdata/reflect.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/testdata/rtti.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/testdata/structreflect.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/testdata/structs.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/testdata/timer.go
/usr/lib/golang/src/golang.org/x/tools/go/pointer/util.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/blockopt.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/builder.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/builder_test.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/const.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/create.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/doc.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/dom.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/emit.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/example_test.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/func.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/external.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/external_darwin.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/external_freebsd.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/external_plan9.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/external_unix.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/external_windows.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/interp.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/interp_test.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/map.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/ops.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/reflect.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/testdata/a_test.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/testdata/b_test.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/testdata/boundmeth.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/testdata/callstack.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/testdata/complit.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/testdata/coverage.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/testdata/defer.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/testdata/fieldprom.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/testdata/ifaceconv.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/testdata/ifaceprom.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/testdata/initorder.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/testdata/methprom.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/testdata/mrvchain.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/testdata/range.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/testdata/recover.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/testdata/reflect.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/testdata/static.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/interp/value.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/lift.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/lvalue.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/methods.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/mode.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/print.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/sanity.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/source.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/source_test.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/ssa.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/ssautil/load.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/ssautil/load_test.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/ssautil/switch.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/ssautil/switch_test.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/ssautil/testdata/switches.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/ssautil/visit.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/stdlib_test.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/testdata/objlookup.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/testdata/valueforexpr.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/testmain.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/testmain_test.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/util.go
/usr/lib/golang/src/golang.org/x/tools/go/ssa/wrappers.go
/usr/lib/golang/src/golang.org/x/tools/go/types/api.go
/usr/lib/golang/src/golang.org/x/tools/go/types/api_test.go
/usr/lib/golang/src/golang.org/x/tools/go/types/assignments.go
/usr/lib/golang/src/golang.org/x/tools/go/types/builtins.go
/usr/lib/golang/src/golang.org/x/tools/go/types/builtins_test.go
/usr/lib/golang/src/golang.org/x/tools/go/types/call.go
/usr/lib/golang/src/golang.org/x/tools/go/types/check.go
/usr/lib/golang/src/golang.org/x/tools/go/types/check_test.go
/usr/lib/golang/src/golang.org/x/tools/go/types/conversions.go
/usr/lib/golang/src/golang.org/x/tools/go/types/decl.go
/usr/lib/golang/src/golang.org/x/tools/go/types/errors.go
/usr/lib/golang/src/golang.org/x/tools/go/types/eval.go
/usr/lib/golang/src/golang.org/x/tools/go/types/eval_test.go
/usr/lib/golang/src/golang.org/x/tools/go/types/expr.go
/usr/lib/golang/src/golang.org/x/tools/go/types/exprstring.go
/usr/lib/golang/src/golang.org/x/tools/go/types/exprstring_test.go
/usr/lib/golang/src/golang.org/x/tools/go/types/go11.go
/usr/lib/golang/src/golang.org/x/tools/go/types/go12.go
/usr/lib/golang/src/golang.org/x/tools/go/types/hilbert_test.go
/usr/lib/golang/src/golang.org/x/tools/go/types/initorder.go
/usr/lib/golang/src/golang.org/x/tools/go/types/issues_test.go
/usr/lib/golang/src/golang.org/x/tools/go/types/labels.go
/usr/lib/golang/src/golang.org/x/tools/go/types/lookup.go
/usr/lib/golang/src/golang.org/x/tools/go/types/methodset.go
/usr/lib/golang/src/golang.org/x/tools/go/types/object.go
/usr/lib/golang/src/golang.org/x/tools/go/types/objset.go
/usr/lib/golang/src/golang.org/x/tools/go/types/operand.go
/usr/lib/golang/src/golang.org/x/tools/go/types/ordering.go
/usr/lib/golang/src/golang.org/x/tools/go/types/package.go
/usr/lib/golang/src/golang.org/x/tools/go/types/predicates.go
/usr/lib/golang/src/golang.org/x/tools/go/types/resolver.go
/usr/lib/golang/src/golang.org/x/tools/go/types/resolver_test.go
/usr/lib/golang/src/golang.org/x/tools/go/types/return.go
/usr/lib/golang/src/golang.org/x/tools/go/types/scope.go
/usr/lib/golang/src/golang.org/x/tools/go/types/selection.go
/usr/lib/golang/src/golang.org/x/tools/go/types/self_test.go
/usr/lib/golang/src/golang.org/x/tools/go/types/sizes.go
/usr/lib/golang/src/golang.org/x/tools/go/types/stdlib_test.go
/usr/lib/golang/src/golang.org/x/tools/go/types/stmt.go
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/blank.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/builtins.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/const0.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/const1.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/constdecl.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/conversions.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/cycles.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/cycles1.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/cycles2.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/cycles3.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/cycles4.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/decls0.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/decls1.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/decls2a.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/decls2b.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/decls3.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/errors.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/expr0.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/expr1.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/expr2.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/expr3.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/gotos.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/importdecl0a.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/importdecl0b.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/importdecl1a.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/importdecl1b.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/init0.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/init1.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/init2.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/issues.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/labels.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/methodsets.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/shifts.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/stmt0.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/stmt1.src
/usr/lib/golang/src/golang.org/x/tools/go/types/testdata/vardecl.src
/usr/lib/golang/src/golang.org/x/tools/go/types/token_test.go
/usr/lib/golang/src/golang.org/x/tools/go/types/type.go
/usr/lib/golang/src/golang.org/x/tools/go/types/typestring.go
/usr/lib/golang/src/golang.org/x/tools/go/types/typestring_test.go
/usr/lib/golang/src/golang.org/x/tools/go/types/typeutil/example_test.go
/usr/lib/golang/src/golang.org/x/tools/go/types/typeutil/imports.go
/usr/lib/golang/src/golang.org/x/tools/go/types/typeutil/imports_test.go
/usr/lib/golang/src/golang.org/x/tools/go/types/typeutil/map.go
/usr/lib/golang/src/golang.org/x/tools/go/types/typeutil/map_test.go
/usr/lib/golang/src/golang.org/x/tools/go/types/typeutil/methodsetcache.go
/usr/lib/golang/src/golang.org/x/tools/go/types/typeutil/ui.go
/usr/lib/golang/src/golang.org/x/tools/go/types/typexpr.go
/usr/lib/golang/src/golang.org/x/tools/go/types/universe.go
/usr/lib/golang/src/golang.org/x/tools/go/vcs/discovery.go
/usr/lib/golang/src/golang.org/x/tools/go/vcs/env.go
/usr/lib/golang/src/golang.org/x/tools/go/vcs/http.go
/usr/lib/golang/src/golang.org/x/tools/go/vcs/vcs.go
/usr/lib/golang/src/golang.org/x/tools/go/vcs/vcs_test.go
/usr/lib/golang/src/golang.org/x/tools/godoc/analysis/analysis.go
/usr/lib/golang/src/golang.org/x/tools/godoc/analysis/callgraph.go
/usr/lib/golang/src/golang.org/x/tools/godoc/analysis/implements.go
/usr/lib/golang/src/golang.org/x/tools/godoc/analysis/json.go
/usr/lib/golang/src/golang.org/x/tools/godoc/analysis/peers.go
/usr/lib/golang/src/golang.org/x/tools/godoc/analysis/typeinfo.go
/usr/lib/golang/src/golang.org/x/tools/godoc/appengine.go
/usr/lib/golang/src/golang.org/x/tools/godoc/cmdline.go
/usr/lib/golang/src/golang.org/x/tools/godoc/cmdline_test.go
/usr/lib/golang/src/golang.org/x/tools/godoc/corpus.go
/usr/lib/golang/src/golang.org/x/tools/godoc/dirtrees.go
/usr/lib/golang/src/golang.org/x/tools/godoc/dl/dl.go
/usr/lib/golang/src/golang.org/x/tools/godoc/dl/dl_test.go
/usr/lib/golang/src/golang.org/x/tools/godoc/dl/tmpl.go
/usr/lib/golang/src/golang.org/x/tools/godoc/format.go
/usr/lib/golang/src/golang.org/x/tools/godoc/godoc.go
/usr/lib/golang/src/golang.org/x/tools/godoc/godoc_test.go
/usr/lib/golang/src/golang.org/x/tools/godoc/index.go
/usr/lib/golang/src/golang.org/x/tools/godoc/index_test.go
/usr/lib/golang/src/golang.org/x/tools/godoc/linkify.go
/usr/lib/golang/src/golang.org/x/tools/godoc/meta.go
/usr/lib/golang/src/golang.org/x/tools/godoc/page.go
/usr/lib/golang/src/golang.org/x/tools/godoc/parser.go
/usr/lib/golang/src/golang.org/x/tools/godoc/pres.go
/usr/lib/golang/src/golang.org/x/tools/godoc/proxy/appengine.go
/usr/lib/golang/src/golang.org/x/tools/godoc/proxy/proxy.go
/usr/lib/golang/src/golang.org/x/tools/godoc/redirect/hash.go
/usr/lib/golang/src/golang.org/x/tools/godoc/redirect/redirect.go
/usr/lib/golang/src/golang.org/x/tools/godoc/search.go
/usr/lib/golang/src/golang.org/x/tools/godoc/server.go
/usr/lib/golang/src/golang.org/x/tools/godoc/short/short.go
/usr/lib/golang/src/golang.org/x/tools/godoc/short/tmpl.go
/usr/lib/golang/src/golang.org/x/tools/godoc/snippet.go
/usr/lib/golang/src/golang.org/x/tools/godoc/spec.go
/usr/lib/golang/src/golang.org/x/tools/godoc/spot.go
/usr/lib/golang/src/golang.org/x/tools/godoc/static/doc.go
/usr/lib/golang/src/golang.org/x/tools/godoc/static/gen.go
/usr/lib/golang/src/golang.org/x/tools/godoc/static/makestatic.go
/usr/lib/golang/src/golang.org/x/tools/godoc/static/static.go
/usr/lib/golang/src/golang.org/x/tools/godoc/tab.go
/usr/lib/golang/src/golang.org/x/tools/godoc/template.go
/usr/lib/golang/src/golang.org/x/tools/godoc/util/throttle.go
/usr/lib/golang/src/golang.org/x/tools/godoc/util/util.go
/usr/lib/golang/src/golang.org/x/tools/godoc/vfs/gatefs/gatefs.go
/usr/lib/golang/src/golang.org/x/tools/godoc/vfs/httpfs/httpfs.go
/usr/lib/golang/src/golang.org/x/tools/godoc/vfs/mapfs/mapfs.go
/usr/lib/golang/src/golang.org/x/tools/godoc/vfs/mapfs/mapfs_test.go
/usr/lib/golang/src/golang.org/x/tools/godoc/vfs/namespace.go
/usr/lib/golang/src/golang.org/x/tools/godoc/vfs/os.go
/usr/lib/golang/src/golang.org/x/tools/godoc/vfs/vfs.go
/usr/lib/golang/src/golang.org/x/tools/godoc/vfs/zipfs/zipfs.go
/usr/lib/golang/src/golang.org/x/tools/imports/fix.go
/usr/lib/golang/src/golang.org/x/tools/imports/fix_test.go
/usr/lib/golang/src/golang.org/x/tools/imports/imports.go
/usr/lib/golang/src/golang.org/x/tools/imports/mkindex.go
/usr/lib/golang/src/golang.org/x/tools/imports/mkstdlib.go
/usr/lib/golang/src/golang.org/x/tools/imports/sortimports.go
/usr/lib/golang/src/golang.org/x/tools/imports/sortimports_compat.go
/usr/lib/golang/src/golang.org/x/tools/imports/zstdlib.go
/usr/lib/golang/src/golang.org/x/tools/oracle/callees.go
/usr/lib/golang/src/golang.org/x/tools/oracle/callers.go
/usr/lib/golang/src/golang.org/x/tools/oracle/callstack.go
/usr/lib/golang/src/golang.org/x/tools/oracle/definition.go
/usr/lib/golang/src/golang.org/x/tools/oracle/describe.go
/usr/lib/golang/src/golang.org/x/tools/oracle/freevars.go
/usr/lib/golang/src/golang.org/x/tools/oracle/implements.go
/usr/lib/golang/src/golang.org/x/tools/oracle/oracle.go
/usr/lib/golang/src/golang.org/x/tools/oracle/oracle_test.go
/usr/lib/golang/src/golang.org/x/tools/oracle/peers.go
/usr/lib/golang/src/golang.org/x/tools/oracle/pointsto.go
/usr/lib/golang/src/golang.org/x/tools/oracle/pos.go
/usr/lib/golang/src/golang.org/x/tools/oracle/referrers.go
/usr/lib/golang/src/golang.org/x/tools/oracle/serial/serial.go
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/calls-json/main.go
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/calls-json/main.golden
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/calls/main.go
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/calls/main.golden
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/describe-json/main.go
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/describe-json/main.golden
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/describe/main.go
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/describe/main.golden
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/freevars/main.go
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/freevars/main.golden
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/implements-json/main.go
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/implements-json/main.golden
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/implements-methods-json/main.go
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/implements-methods-json/main.golden
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/implements-methods/main.go
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/implements-methods/main.golden
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/implements/main.go
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/implements/main.golden
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/imports/main.go
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/imports/main.golden
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/lib/lib.go
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/main/multi.go
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/peers-json/main.go
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/peers-json/main.golden
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/peers/main.go
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/peers/main.golden
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/pointsto-json/main.go
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/pointsto-json/main.golden
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/pointsto/main.go
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/pointsto/main.golden
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/referrers-json/main.go
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/referrers-json/main.golden
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/referrers/ext_test.go
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/referrers/int_test.go
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/referrers/main.go
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/referrers/main.golden
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/reflection/main.go
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/reflection/main.golden
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/what-json/main.go
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/what-json/main.golden
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/what/main.go
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/what/main.golden
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/whicherrs/main.go
/usr/lib/golang/src/golang.org/x/tools/oracle/testdata/src/whicherrs/main.golden
/usr/lib/golang/src/golang.org/x/tools/oracle/what.go
/usr/lib/golang/src/golang.org/x/tools/oracle/whicherrs.go
/usr/lib/golang/src/golang.org/x/tools/playground/appengine.go
/usr/lib/golang/src/golang.org/x/tools/playground/appenginevm.go
/usr/lib/golang/src/golang.org/x/tools/playground/common.go
/usr/lib/golang/src/golang.org/x/tools/playground/local.go
/usr/lib/golang/src/golang.org/x/tools/playground/socket/socket.go
/usr/lib/golang/src/golang.org/x/tools/present/args.go
/usr/lib/golang/src/golang.org/x/tools/present/caption.go
/usr/lib/golang/src/golang.org/x/tools/present/code.go
/usr/lib/golang/src/golang.org/x/tools/present/doc.go
/usr/lib/golang/src/golang.org/x/tools/present/html.go
/usr/lib/golang/src/golang.org/x/tools/present/iframe.go
/usr/lib/golang/src/golang.org/x/tools/present/image.go
/usr/lib/golang/src/golang.org/x/tools/present/link.go
/usr/lib/golang/src/golang.org/x/tools/present/link_test.go
/usr/lib/golang/src/golang.org/x/tools/present/parse.go
/usr/lib/golang/src/golang.org/x/tools/present/style.go
/usr/lib/golang/src/golang.org/x/tools/present/style_test.go
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/eg.go
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/eg_test.go
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/match.go
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/rewrite.go
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/A.template
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/A1.go
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/A1.golden
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/A2.go
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/A2.golden
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/B.template
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/B1.go
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/B1.golden
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/C.template
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/C1.go
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/C1.golden
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/D.template
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/D1.go
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/D1.golden
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/E.template
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/E1.go
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/E1.golden
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/F.template
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/F1.go
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/F1.golden
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/G.template
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/G1.go
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/G1.golden
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/H.template
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/H1.go
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/H1.golden
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/bad_type.template
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/expr_type_mismatch.template
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/no_after_return.template
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/no_before.template
/usr/lib/golang/src/golang.org/x/tools/refactor/eg/testdata/type_mismatch.template
/usr/lib/golang/src/golang.org/x/tools/refactor/importgraph/graph.go
/usr/lib/golang/src/golang.org/x/tools/refactor/importgraph/graph_test.go
/usr/lib/golang/src/golang.org/x/tools/refactor/rename/check.go
/usr/lib/golang/src/golang.org/x/tools/refactor/rename/mvpkg.go
/usr/lib/golang/src/golang.org/x/tools/refactor/rename/mvpkg_test.go
/usr/lib/golang/src/golang.org/x/tools/refactor/rename/rename.go
/usr/lib/golang/src/golang.org/x/tools/refactor/rename/rename_test.go
/usr/lib/golang/src/golang.org/x/tools/refactor/rename/spec.go
/usr/lib/golang/src/golang.org/x/tools/refactor/rename/util.go
/usr/lib/golang/src/golang.org/x/tools/refactor/satisfy/find.go
