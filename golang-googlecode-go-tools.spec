Name     : golang-googlecode-go-tools 
Version  : 0
Release  : 7
URL      : https://github.com/golang/tools/archive/f2932db7c0155d2ea19373270a3fa937349ac375.tar.gz
Source0  : https://github.com/golang/tools/archive/f2932db7c0155d2ea19373270a3fa937349ac375.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
BuildRequires : go
BuildRequires : golang-googlecode-go-net

%description
This subrepository holds the source for various packages and tools that support
the Go programming language.

%package bin
Summary: bin components for the golang-googlecode-go-tools package.
Group: Binaries

%description bin
bin components for the golang-googlecode-go-tools package.

%prep
%setup -q -n tools-f2932db7c0155d2ea19373270a3fa937349ac375

%build
mkdir -p build-dir/src/golang.org/x
ln -s $(pwd) build-dir/src/golang.org/x/tools
export GOPATH=$(pwd)/build-dir:/usr/lib/golang
pushd build-dir
for cmd in \
    benchcmp \
    bundle \
    callgraph \
    cover \
    digraph \
    eg \
    fiximports \
    godex \
    godoc \
    goimports \
    gomvpkg \
    gorename \
    gotype \
    guru \
    html2article \
    oracle \
    present \
    ssadump \
    stress \
    stringer \
    tip

do
    go build golang.org/x/tools/cmd/$cmd
done
popd


%install
rm -rf %{buildroot}
%global gopath /usr/lib/golang
%global library_path golang.org/x/tools
mkdir -p %{buildroot}/usr/bin 

install -p -m 755 build-dir/benchcmp %{buildroot}/usr/bin
install -p -m 755 build-dir/bundle %{buildroot}/usr/bin
install -p -m 755 build-dir/callgraph %{buildroot}/usr/bin
install -p -m 755 build-dir/cover %{buildroot}/usr/bin
install -p -m 755 build-dir/digraph %{buildroot}/usr/bin
install -p -m 755 build-dir/eg %{buildroot}/usr/bin
install -p -m 755 build-dir/fiximports %{buildroot}/usr/bin
install -p -m 755 build-dir/godex %{buildroot}/usr/bin
install -p -m 755 build-dir/godoc %{buildroot}/usr/bin
install -p -m 755 build-dir/goimports %{buildroot}/usr/bin
install -p -m 755 build-dir/gomvpkg %{buildroot}/usr/bin
install -p -m 755 build-dir/gorename %{buildroot}/usr/bin
install -p -m 755 build-dir/gotype %{buildroot}/usr/bin
install -p -m 755 build-dir/guru %{buildroot}/usr/bin
install -p -m 755 build-dir/html2article %{buildroot}/usr/bin
install -p -m 755 build-dir/oracle %{buildroot}/usr/bin
install -p -m 755 build-dir/present %{buildroot}/usr/bin
install -p -m 755 build-dir/ssadump %{buildroot}/usr/bin
install -p -m 755 build-dir/stress %{buildroot}/usr/bin
install -p -m 755 build-dir/stringer %{buildroot}/usr/bin
install -p -m 755 build-dir/tip %{buildroot}/usr/bin

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
go test %{library_path}/... || :

%files bin
%defattr(-,root,root,-)
/usr/bin/benchcmp
/usr/bin/bundle
/usr/bin/callgraph
/usr/bin/cover
/usr/bin/digraph
/usr/bin/eg
/usr/bin/fiximports
/usr/bin/godex
/usr/bin/godoc
/usr/bin/goimports
/usr/bin/gomvpkg
/usr/bin/gorename
/usr/bin/gotype
/usr/bin/guru
/usr/bin/html2article
/usr/bin/oracle
/usr/bin/present
/usr/bin/ssadump
/usr/bin/stress
/usr/bin/stringer
/usr/bin/tip

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
/usr/lib/golang/src/golang.org/x/tools/cmd/bundle/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/bundle/main_test.go
/usr/lib/golang/src/golang.org/x/tools/cmd/bundle/testdata/out.golden
/usr/lib/golang/src/golang.org/x/tools/cmd/bundle/testdata/src/domain.name/importdecl/p.go
/usr/lib/golang/src/golang.org/x/tools/cmd/bundle/testdata/src/initial/a.go
/usr/lib/golang/src/golang.org/x/tools/cmd/bundle/testdata/src/initial/b.go
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
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/callees.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/callers.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/callstack.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/definition.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/describe.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/freevars.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/guru.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/guru_test.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/implements.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/peers.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/pointsto.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/pos.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/referrers.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/serial/serial.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/calls-json/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/calls-json/main.golden
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/calls/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/calls/main.golden
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/definition-json/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/definition-json/main.golden
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/describe-json/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/describe-json/main.golden
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/describe/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/describe/main.golden
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/freevars/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/freevars/main.golden
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/implements-json/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/implements-json/main.golden
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/implements-methods-json/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/implements-methods-json/main.golden
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/implements-methods/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/implements-methods/main.golden
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/implements/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/implements/main.golden
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/imports/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/imports/main.golden
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/lib/lib.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/main/multi.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/peers-json/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/peers-json/main.golden
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/peers/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/peers/main.golden
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/pointsto-json/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/pointsto-json/main.golden
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/pointsto/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/pointsto/main.golden
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/referrers-json/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/referrers-json/main.golden
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/referrers/ext_test.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/referrers/int_test.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/referrers/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/referrers/main.golden
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/reflection/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/reflection/main.golden
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/what-json/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/what-json/main.golden
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/what/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/what/main.golden
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/whicherrs/main.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/testdata/src/whicherrs/main.golden
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/what.go
/usr/lib/golang/src/golang.org/x/tools/cmd/guru/whicherrs.go
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
/usr/lib/golang/src/golang.org/x/tools/container/intsets/popcnt_amd64.go
/usr/lib/golang/src/golang.org/x/tools/container/intsets/popcnt_amd64.s
/usr/lib/golang/src/golang.org/x/tools/container/intsets/popcnt_gccgo.go
/usr/lib/golang/src/golang.org/x/tools/container/intsets/popcnt_generic.go
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
/usr/lib/golang/src/golang.org/x/tools/go/buildutil/overlay.go
/usr/lib/golang/src/golang.org/x/tools/go/buildutil/overlay_test.go
/usr/lib/golang/src/golang.org/x/tools/go/buildutil/tags.go
/usr/lib/golang/src/golang.org/x/tools/go/buildutil/tags_test.go
/usr/lib/golang/src/golang.org/x/tools/go/buildutil/util.go
/usr/lib/golang/src/golang.org/x/tools/go/buildutil/util_test.go
/usr/lib/golang/src/golang.org/x/tools/go/buildutil/util_windows_test.go
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
/usr/lib/golang/src/golang.org/x/tools/go/gcimporter15/bexport.go
/usr/lib/golang/src/golang.org/x/tools/go/gcimporter15/bexport_test.go
/usr/lib/golang/src/golang.org/x/tools/go/gcimporter15/bimport.go
/usr/lib/golang/src/golang.org/x/tools/go/gcimporter15/exportdata.go
/usr/lib/golang/src/golang.org/x/tools/go/gcimporter15/gcimporter.go
/usr/lib/golang/src/golang.org/x/tools/go/gcimporter15/gcimporter17_test.go
/usr/lib/golang/src/golang.org/x/tools/go/gcimporter15/gcimporter_test.go
/usr/lib/golang/src/golang.org/x/tools/go/gcimporter15/setname15.go
/usr/lib/golang/src/golang.org/x/tools/go/gcimporter15/setname16.go
/usr/lib/golang/src/golang.org/x/tools/go/gcimporter15/setname_test.go
/usr/lib/golang/src/golang.org/x/tools/go/gcimporter15/testdata/a.go
/usr/lib/golang/src/golang.org/x/tools/go/gcimporter15/testdata/b.go
/usr/lib/golang/src/golang.org/x/tools/go/gcimporter15/testdata/exports.go
/usr/lib/golang/src/golang.org/x/tools/go/gcimporter15/testdata/issue15920.go
/usr/lib/golang/src/golang.org/x/tools/go/gcimporter15/testdata/p.go
/usr/lib/golang/src/golang.org/x/tools/go/loader/cgo.go
/usr/lib/golang/src/golang.org/x/tools/go/loader/cgo_pkgconfig.go
/usr/lib/golang/src/golang.org/x/tools/go/loader/doc.go
/usr/lib/golang/src/golang.org/x/tools/go/loader/example15_test.go
/usr/lib/golang/src/golang.org/x/tools/go/loader/example_test.go
/usr/lib/golang/src/golang.org/x/tools/go/loader/go16.go
/usr/lib/golang/src/golang.org/x/tools/go/loader/go16_test.go
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
/usr/lib/golang/src/golang.org/x/tools/go/ssa/const15.go
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
/usr/lib/golang/src/golang.org/x/tools/go/types/typeutil/example_test.go
/usr/lib/golang/src/golang.org/x/tools/go/types/typeutil/imports.go
/usr/lib/golang/src/golang.org/x/tools/go/types/typeutil/imports_test.go
/usr/lib/golang/src/golang.org/x/tools/go/types/typeutil/map.go
/usr/lib/golang/src/golang.org/x/tools/go/types/typeutil/map_test.go
/usr/lib/golang/src/golang.org/x/tools/go/types/typeutil/methodsetcache.go
/usr/lib/golang/src/golang.org/x/tools/go/types/typeutil/ui.go
/usr/lib/golang/src/golang.org/x/tools/go/types/typeutil/ui_test.go
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
/usr/lib/golang/src/golang.org/x/tools/godoc/proxy/proxy.go
/usr/lib/golang/src/golang.org/x/tools/godoc/redirect/hash.go
/usr/lib/golang/src/golang.org/x/tools/godoc/redirect/redirect.go
/usr/lib/golang/src/golang.org/x/tools/godoc/redirect/redirect_test.go
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
/usr/lib/golang/src/golang.org/x/tools/godoc/vfs/emptyvfs.go
/usr/lib/golang/src/golang.org/x/tools/godoc/vfs/emptyvfs_test.go
/usr/lib/golang/src/golang.org/x/tools/godoc/vfs/gatefs/gatefs.go
/usr/lib/golang/src/golang.org/x/tools/godoc/vfs/httpfs/httpfs.go
/usr/lib/golang/src/golang.org/x/tools/godoc/vfs/mapfs/mapfs.go
/usr/lib/golang/src/golang.org/x/tools/godoc/vfs/mapfs/mapfs_test.go
/usr/lib/golang/src/golang.org/x/tools/godoc/vfs/namespace.go
/usr/lib/golang/src/golang.org/x/tools/godoc/vfs/os.go
/usr/lib/golang/src/golang.org/x/tools/godoc/vfs/vfs.go
/usr/lib/golang/src/golang.org/x/tools/godoc/vfs/zipfs/zipfs.go
/usr/lib/golang/src/golang.org/x/tools/godoc/vfs/zipfs/zipfs_test.go
/usr/lib/golang/src/golang.org/x/tools/imports/fix.go
/usr/lib/golang/src/golang.org/x/tools/imports/fix_test.go
/usr/lib/golang/src/golang.org/x/tools/imports/imports.go
/usr/lib/golang/src/golang.org/x/tools/imports/mkindex.go
/usr/lib/golang/src/golang.org/x/tools/imports/mkstdlib.go
/usr/lib/golang/src/golang.org/x/tools/imports/sortimports.go
/usr/lib/golang/src/golang.org/x/tools/imports/zstdlib.go
/usr/lib/golang/src/golang.org/x/tools/oracle/callees.go
/usr/lib/golang/src/golang.org/x/tools/oracle/callers.go
/usr/lib/golang/src/golang.org/x/tools/oracle/callstack.go
/usr/lib/golang/src/golang.org/x/tools/oracle/definition.go
/usr/lib/golang/src/golang.org/x/tools/oracle/describe.go
/usr/lib/golang/src/golang.org/x/tools/oracle/describe15.go
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
/usr/lib/golang/src/golang.org/x/tools/playground/socket/socket_test.go
/usr/lib/golang/src/golang.org/x/tools/present/args.go
/usr/lib/golang/src/golang.org/x/tools/present/background.go
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
/usr/lib/golang/src/golang.org/x/tools/present/video.go
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
